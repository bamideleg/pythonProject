
from selenium import webdriver
import time
import unittest



class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/bamid/PycharmProjects/pythonProject/browserDrivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin") # To comment all the code ctrl + / (forward slash)
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(5)



    @classmethod
    def teadDownClass(cls):  # run only when all test are completed.
            #  def teadDown(self): # It will run after a very test
            #cls.driver.quit()
            cls.driver.close()
            print("Test completed")

if __name__== '__main__': # The purpose is to directly run the test from CMD line by simply enter = python (test name) as python login.py
    unittest.main()
