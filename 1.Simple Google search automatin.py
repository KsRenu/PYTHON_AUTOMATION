from selenium import webdriver 
import time
find=input("Enter what you need to search : ")
browser=webdriver.Chrome(executable_path="C:\\Users\\Admin\\Downloads\\chromedriver_win32\\chromedriver") 
browser.get('https://www.google.com/')
time.sleep(3)
search_input=browser.find_element_by_name('q')
search_input.send_keys(find)
time.sleep(2)
search_btn=browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()