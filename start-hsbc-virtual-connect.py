from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

passcode = input("Please input passcode from SecurID app: ")

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)

## Go to the website
driver.get("https://tko.exconnect.hsbc.com.hk/logon/LogonPoint/tmindex.html")

login_box = driver.find_element_by_id("login")
login_box.send_keys('45244360')

password_box = driver.find_element_by_id('passwd1')
password_box.send_keys('Pr92180709')

passcode_box = driver.find_element_by_id('passwd')
passcode_box.send_keys(passcode)

# login_box.send_keys(Keys.ENTER)
# login_box.submit()
## End the session 
# driver.close()
