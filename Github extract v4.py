
# this will extract complete user info on command prompt on URl Based

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


def main():
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
    
    driver.get('https://github.com/search?l=Java&p=25&q=%22BIg+Data%22&type=Users')

    #___________________Done_______________________#

    pages_remaining = True
 
    while pages_remaining:
        soup = bs.BeautifulSoup(driver.page_source,'lxml')
        #Data from users
        for users in soup.find_all(class_="user-list-item py-4 d-flex hx_hit-user"):  #previous  user-list-info ml-2 min-width-0
            print(users.text)
            print("+-"*30,"\n\n")
            
        try:
            #Checks if there are more pages with links
            next_link = driver.find_element_by_class_name('next_page')
            next_link.click()
            time.sleep(4)
        except NoSuchElementException:
            rows_remaining = False

    
if __name__ == '__main__':
    main()

