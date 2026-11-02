from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)

## Go to the website
driver.get("https://realpython.com/")
## Find the login button and click it
login_button = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a')
login_button.submit()

# login_box.send_keys(Keys.ENTER)
# login_box.submit()
## End the session 
# driver.close()
