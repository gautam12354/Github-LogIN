#simple code for github account login
from selenium import webdriver
import time

def main():
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    driver.get('https://github.com/')
    sign_in = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    sign_in.click()
    userid = driver.find_element_by_id("login_field")
    userid.send_keys('Your Email Here')                                     #put here your Email
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('your git password')                                 #your git pass 
    submit = driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]')
    submit.click()
    time.sleep(2000)
    
    
if __name__ == '__main__':
    main()
