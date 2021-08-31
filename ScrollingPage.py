

#https://www.youtube.com/watch?v=o3tYiyE_OXE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://mybarnite.com/#")
#driver.maximize_window()




# Stroll page until it is visible
flag= driver.find_element_by_xpath("")
driver.execute_script("argument[0].ScrollIntoView():",flag)



# Stroll unitil the end of page
#driver.execute_script("window.strollBy(0,document.body.scrollHeight)")