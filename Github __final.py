#complete user class = user-list-info ml-2 min-width-0

#name class  = d-block d-md-inline f4 mt-2 mt-md-0 ml-md-1
#email class  = muted-link
#discription class  = f5 mt-2


#https://github.com/search?q=%22linkedin%22+OR+Hadoop&type=Users
# Keyword --> "linkedin" OR Hadoop
# Script Name           : Github extract.py
# Author                : Gautam Kumar Pandey
# Created               : 17th May 2019
# Last Modified         : 
# Version               : 1.0
# Description           : Extract Emails and other Information from Github for users

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import bs4 as bs
import csv
import time

f = csv.writer(open("githubData.csv", "w"))
f.writerow(["Name","Discription","Email"])


driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.get('https://github.com/')
sign_in = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
sign_in.click()
userid = driver.find_element_by_id("login_field")
userid.send_keys('gautamk780@gmail.com')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('gitpygautam123')
submit = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]')     
submit.click() 
time.sleep(5)

#locate Search feild
search = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]')

#type text here
search.send_keys('"data analytics"')
search.send_keys(Keys.RETURN)
time.sleep(5)

#Locate users and click
users= driver.find_element_by_css_selector('#js-pjax-container > div > div.col-12.col-md-3.float-left.px-md-2 > nav.menu.border.d-none.d-md-block > a:nth-child(9)')
users.click()
time.sleep(5)

#___________________Done_______________________#

pages_remaining = True

while pages_remaining:
    soup = bs.BeautifulSoup(driver.page_source,'lxml')
    #Data from users

    name = soup.find_all(class_="d-block d-md-inline f4 mt-2 mt-md-0 ml-md-1")
    dis = soup.find_all(class_="f5 mt-2")
    email = soup.find_all(class_="muted-link")

    for data in name:
        n = data.text
        f.writerow([n])

        for dat in dis:
            d= dat.text
            f.writerow([d])

        for da in email:
            e = da.text
            f.writerow([e])
        
    try:
        #Checks if there are more pages with links
        next_link = driver.find_element_by_class_name('next_page')
        next_link.click()
        time.sleep(4)
    except NoSuchElementException:
        rows_remaining = False


