from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
#print(pyperclip.__version__)
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome(executable_path="F:\\GitHub\\pythonAutomation\\chromedriver_win32\\chromedriver") 
browser.maximize_window()
browser.get('https://web.whatsapp.com/')
time.sleep(2)

with open('F:/GitHub/pythonAutomation/3.Whatsapp automation/groups.txt','r') as f: 
    #to fetch the groups
    groups=[group.strip() for group in f.readlines()]
with open('F:/GitHub/pythonAutomation/3.Whatsapp automation/msg.txt','r',encoding='utf8') as f:
    msg=f.read()
time.sleep(30)
for group in groups :
    search_xpath='//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until( 
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    search_box.clear()
    time.sleep(1)
    pyperclip.copy(group)
    from selenium.webdriver.common.keys import Keys
    search_box.send_keys( Keys.CONTROL + "v") 
    time.sleep(2)
    group_xpath=f'//span[@title="{group}"]'
    #group_title=browser.find_element_by_xpath(group_xpath)
    group_title=browser.find_element(By.XPATH,group_xpath)
    group_title.click()
    time.sleep(1)
    input_xpath='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    #input_box=browser.find_element_by_xpath(input_xpath)
    input_box=browser.find_element(By.XPATH,input_xpath)
    pyperclip.copy(msg)
    input_box.send_keys( Keys.CONTROL + "v") 
    input_box.send_keys(Keys.ENTER)
    time.sleep(2) 