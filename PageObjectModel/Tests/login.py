# https://www.youtube.com/watch?v=BURK7wMcCwU
# Selenium Python Small Sample Project | Page Object Model POM

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import unittest
from PageObjectModel.Pages.loginPage import loginPage
from PageObjectModel.Pages.HomePage import Homepage


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/bamid/PycharmProjects/pythonProject/browserDrivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    #    cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = loginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_button()



        homePage=Homepage(driver)
        homePage.click_welcome()
        homePage.click_logout()

        time.sleep(2)

    @classmethod
    def teadDownClass(cls):  # run only when all test are completed.
        #  def teadDown(self): # It will run after a very test
        # cls.driver.quit()
        cls.driver.close()

        print("Test completed")


if __name__ == '__main__':  # The purpose is to directly run the test from CMD line by simply enter = python (test name) as python login.py
    unittest.main()
