from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver.get("https://www.psegameshop.com/my-account/")
print(driver.title)
time.sleep(3)

#click lupa password
lupa_password = driver.find_element_by_link_text("Lost your password?")
lupa_password.click()

input_username = driver.find_element_by_id("user_login")
input_username.send_keys("rimasirfansyah12@gmail.com")
btn_reset = driver.find_element_by_xpath('//button[text()="Reset password"]')
btn_reset.click()
time.sleep(1)

#print(driver.page_source) to print html

