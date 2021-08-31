
#https://www.youtube.com/watch?v=o3tYiyE_OXE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver=webdriver.Chrome(executable_path=".\\Browsers/chromedriver.exe")
print("launching chrome browser")

driver.get("https://www.mybarnite.com/")

links=driver.find_elements(By.TAG_NAME,"a")
print("The number of link present:",len(links))

driver.find_element(By.NAME,"cat").send_keys("Lounges")
driver.find_element(By.NAME,"searchtxt").send_keys("TW7")
driver.find_element(By.XPATH,"//button[contains(.,'Search')]").click()
driver.find_element_by_css_selector(".btn-gr-color").click()
time.sleep(3)

pageName=driver.find_element_by_xpath("//div[@id='events_details']/div/div[2]/div/h1").text
print(pageName)

time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'Book seat or Book full bar')]").click()

driver.find_element(By.NAME, "useremail").send_keys("bamglobal95+11@gmail.com")
driver.find_element(By.NAME, "userpassword").send_keys("Password1")

driver.find_element(By.NAME,"loginbut").click()





time.sleep(5)

#driver.close()