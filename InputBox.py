from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.get("https://www.jobserve.com")

time.sleep(3)

driver.find_element_by_id("loginMnu").is_displayed()

drp=driver.find_element_by_id("loginMnu").click()
driver.find_element_by_css_selector(".active li:nth-child(1) > a").click()
time.sleep(3)
driver.find_element(By.ID, "PolicyOptInLink").click()

#element=driver.find_element_by_css_selector(".active li:nth-child(1) > a")
#drp=Select(element)
#time.sleep(3)
#drp.select_by_visible_text('Advertisers') # Selec by text
#drp.select_by_index() # Select by index
#drp.select_by_value("")
#print(len (drp.options))  # Count the number of options
#all_options=drp.options # Capture all the options, then output
#for option in all_options:
#    print(option.text)

wait=WebDriverWait(driver,5) # Explicit wait

driver.find_element(By.ID,"txbEmail").send_keys("bamglobal@gmail.com")
driver.find_element(By.ID,"txbPassword").send_keys("Password1")
driver.find_element(By.ID,"btnlogin").click()

driver.find_elements_by_class_name()

time.sleep(3)
driver.close()