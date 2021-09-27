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

fav_genre = driver.find_element_by_id("acf-field_5e758bca4e8cc")
Select(fav_genre).select_by_visible_text("Action")

#sel=Select(fav_genre)
#sel.select_by_visible_text("Action")
time.sleep(1)

fav_console = driver.find_element_by_id("acf-field_5e75905014c81")
Select(fav_console).select_by_value("PC")
time.sleep(1)

hobbies = driver.find_element_by_id("acf-field_5ea976d054e4e")
Select(hobbies).select_by_value("Gadgets & Technology")
time.sleep(1)

gender_male = driver.find_element_by_id("acf-field_5ea3be750efb3-male")
gender_male.click()
time.sleep(1)

reg_email = driver.find_element_by_id("reg_email")
reg_password = driver.find_element_by_id("reg_password")
reg_cpassword = driver.find_element_by_id("reg_confirm_password")

reg_email.send_keys("rimasirfansyah12@gmail.com")
reg_password.send_keys("!niadalahpassword")
reg_cpassword.send_keys("!niadalahpassword")
time.sleep(1)

btn_register = driver.find_element_by_name("register")
btn_register.click()

#print(driver.page_source) to print html

