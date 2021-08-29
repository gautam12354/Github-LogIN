# this will extract emails in csv file

# (["Github_ID","Name","Dicription","LOCATION","Email"])

#https://github.com/search?q=%22linkedin%22+OR+Hadoop&type=Users
# Keyword --> "linkedin" OR Hadoop
# Script Name           : Github extract.py
# Author                : Gautam Kumar Pandey
# Created               : 17th June 2019
# Last Modified         : 
# Version               : 1.0
# Description           : Extract Emails and other Information from Github for users


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import bs4 as bs
from csv import writer
import time



driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.get('https://github.com/')
sign_in = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
sign_in.click()
userid = driver.find_element_by_id("login_field")
userid.send_keys('gautamk780@gmail.com')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('gitpygautam123')
submit = driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
submit.click()
time.sleep(5)

driver.get('https://github.com/search?p=19&q=%22flink%22&type=Users')

#Locate users and click
users= driver.find_element_by_css_selector('#js-pjax-container > div > div.col-12.col-md-3.float-left.px-md-2 > nav.menu.border.d-none.d-md-block > a:nth-child(9)')
users.click()
time.sleep(5)

#___________________Done_______________________#

pages_remaining = True

while pages_remaining:

    with open("github_data.csv", "w") as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(["data"])

        soup = bs.BeautifulSoup(driver.page_source,'lxml')
        #Data from users
        for users in soup.find_all(class_="user-list-item py-4 d-flex hx_hit-user"):  #previous  user-list-info ml-2 min-width-0
            user = users.text
            csv_writer.writerow([user])
            csv_writer.writerow(['**********'])
        
    try:
        #Checks if there are more pages with links
        next_link = driver.find_element_by_class_name('next_page')
        next_link.click()
        time.sleep(4)
    except NoSuchElementException:
        rows_remaining = False


