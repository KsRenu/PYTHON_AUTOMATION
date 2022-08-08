#importing the required libraries
print("Importing the required libraries")
import pandas as pd
import time
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
print("Required libraries are imported successfully")

#updating the chromedriver status
print("updating the chromedriver status")
options = webdriver.ChromeOptions()
options.headless = True
driver=webdriver.Chrome(executable_path="C:\\Users\\Admin\\Downloads\\chromedriver") 
print("Path to the chromedrive has been set")


# opening link part
print("Locating the csv data file for opening the link")
f_path="C:\\Users\\Admin\\Downloads\\posts.csv"
df=pd.read_csv(f_path)
print("File path located successfully")

print("Iterating through all the rows to get all links")
for index, row in df.iterrows():
    link=df.loc[index,'url']
    driver.get(link)
    time.sleep(5)
    S = lambda X: driver.execute_script('return document.body.parentNode.scrollṁ'+X)
    time.sleep(5)
    driver.set_window_size(350,1300) 
    filename=str(index)+'.png'
    #driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
    driver.find_element_by_tag_name('body').screenshot(filename)
    #driver.quit()
    print(index,"Image is captured")
    if index == df.last_valid_index(): #as its for sample i have broken the loop with 10 posts itself
        driver.quit()
        break
print("Process Completed successfully")

#28,76,90
