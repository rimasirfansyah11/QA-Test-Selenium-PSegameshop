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

btn_register = driver.find_element_by_name("register")
btn_register.click()

#print(driver.page_source) to print html

