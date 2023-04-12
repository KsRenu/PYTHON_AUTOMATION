
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
users=['spotknack','spotknack_talent_community'] 
from credentials import USERNAME ,PASSWORD
browser=webdriver.Chrome(executable_path="F:\\GitHub\\pythonAutomation\\chromedriver_win32\\chromedriver") 
browser.get('https://www.instagram.com/')
time.sleep(2)
username_field = browser.find_element("name", 'username')
password_field = browser.find_element("name", 'password')
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_btn=browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_btn.click()
time.sleep(5)
for user in users : 
    browser.get(f"https://www.instagram.com/{user}/")
    time.sleep(5)