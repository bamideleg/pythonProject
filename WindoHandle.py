
#https://www.youtube.com/watch?v=o3tYiyE_OXE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://www.jobserve.com/")

time.sleep(3)

driver.find_element(By.ID,"loginMnu").click()
driver.find_element_by_css_selector(".active li:nth-child(1) > a").click()

print(driver.current_window_handle)

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    # To close a particular window
    if driver.title =="":
       driver.close() # it will close the parent window

    #driver.quit()   # Close all the window
    driver.close() # Close specific window