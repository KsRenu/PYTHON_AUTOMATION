
from selenium import webdriver
import time
users=['_callmenestle_','lakshuguru','s_o_m_e_o_n_e_1628'] 
from credentials import USERNAME ,PASSWORD
browser=webdriver.Chrome(executable_path="C:\\Users\\Admin\\Downloads\\chromedriver_win32\\chromedriver") 
browser.get('https://www.instagram.com/')
time.sleep(2)
username_field = browser.find_element_by_name('username')
password_field = browser.find_element_by_name('password')
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_btn=browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()
time.sleep(5)
for user in users : 
    browser.get(f"https://www.instagram.com/{user}/")