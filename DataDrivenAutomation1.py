
#https://www.youtube.com/watch?v=o3tYiyE_OXE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
#driver.get("https://www.ebay.com/")
driver.get("https://www.ebay.com/")

links=driver.find_elements(By.TAG_NAME,"a")
print("The number of link present A:",len(links))
print("The number of link present B:",len(links))
print("The number of link present C:",len(links))
