
# Automated Framework: it is an organised way of mainitainning automated files. The goals is to create resusable and maintainable


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import unittest
#from PageObjectModel.Pages.RegistrationPage import RegistrationPage
import PageObjectModelProject.Tests.login




class RegistionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="C:/Users/bamid/PycharmProjects/pythonProject/browserDrivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_registration_valid(self):
        driver = self.driver

        self.driver.get("https://www.seleniumeasy.com/test/")

        Registration = RegistrationPage(driver)
        Registration.click_pop_link()
        time.sleep(3)
        Registration.click_inputForm()
        Registration.click_submitForm()
        Registration.enter_firstname("John")
        Registration.enter_lastname("Password1")
        Registration.enter_email("jogn@gmail.com")
        Registration.enter_phone("0786352352363")
        Registration.enter_address("123 london road")
        Registration.enter_city("London")
        Registration.enter_state("Florida")

        Registration.enter_zip("10293839")
        Registration.enter_website("https://johnweb.com")
        Registration.enter_description("Hello world")
        Registration.click_submit()

        time.sleep(5)

        def click_weclome(self):
            self.driver.find_element_by_id(self.welcome_text_id).click()

        def click_logout(self):
                self.driver.find_element_by_link_text(self.logout_link_id).click()


        @classmethod
        def teadDownClass(cls):
                #cls.driver.quit()
                cls.driver.close()
                print("Test completed")

if __name__== '__main__': # The purpose is to directly run the test from CMD line by simply enter = python (test name) as python login.py
    unittest.main()
