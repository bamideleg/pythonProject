
#https://www.youtube.com/watch?v=o3tYiyE_OXE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")


driver.get("https://www.mybarnite.com/")

links=driver.find_elements(By.TAG_NAME,"a")
print("The number of link present:",len(links))

time.sleep(5)

driver.close()