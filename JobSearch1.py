

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.implicitly_wait(5)
driver.get_window_size()
driver.get("https://www.jobserve.com/")

time.sleep(5)

driver.find_element_by_id("txtKey").send_keys("Project Manager")
driver.find_element_by_id("txtLoc").send_keys("Manchester")
driver.find_element_by_id("btnSearch").click()

wait=WebDriverWait(driver,10) # Explicit wait

# how to capture element or expected result
#wait.until(EC.search_number_is_present(driver.find_element_by_id("resultrole")))
element=wait.until(EC.text_to_be_present_in_element((By.ID,"resultrole")))
print(element)


time.sleep(3)

driver.close()
