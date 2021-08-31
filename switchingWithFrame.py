
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.get("https://www.selenium.dev/documentation/en/")

time.sleep(3)

driver.switch_to_frame("")
driver.find_element_by_link_text("").click()

driver.switch_to_default_content()


driver.switch_to_frame("")
driver.find_element_by_link_text("")

driver.switch_to_default_content()

driver.find_elements_by_class_name()

time.sleep(3)
driver.close()