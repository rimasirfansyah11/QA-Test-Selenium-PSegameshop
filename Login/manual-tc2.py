from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.psegameshop.com/my-account/")
print(driver.title)
time.sleep(3)

#define elements
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
btn_login = driver.find_element_by_name("login")

#actions
username.send_keys("rimasirfansyah12@gmail.com")
password.send_keys("p4sswordnyalup4") #correct password  = !nipasswordbaru
btn_login.click()

#print(driver.page_source) to print html

