from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class RegistrationPage():

    def __init__(self, driver): # This is the constructor that we are going to use to link the class
        self.driver = driver

       # element = self.driver.find_element(By.LINK_TEXT, "Alerts & Modals")
       # actions = ActionChains(self.driver)
       # self.click_pop_linkText="No, thanks!"
        self.driver.pop_class="at-cv-button at-cv-lightbox-yesno at-cm-no-button"

        self.click_inputForm_linkText="Input Forms"
        self.click_submit_form_LinkText = "Input Form Submit"
        self.firstname_textbox_name = "first_name"
        self.lastname_textbox_name = "last_name"
        self.email_textbox_name = "email"
        self.phone_number_name = "phone"
        self.address_textbox_name = "address"
        self.city_textbox_name = "city"
        self.state_textbox_name = "state"
        self.zip_textbox_name = "zip"
        self.website_textbox_name = "website"
        self.description_textbox_name = "comment"
        self.submit_button_css_selector=".btn"

    def click_pop_link(self):
        self.driver.driver.find_element_by_link_text(self.click_pop_linkText).click()

    def click_inputForm(self):
        self.driver.find_element_by_link_text(self.click_inputForm_linkText).click()
        #self.driver.find_element(By.LINK_TEXT, "Input Forms").click()

    def click_submitForm(self):
            self.driver.find_element_by_id(self.click_submit_form_LinkText).click()

    def enter_firstname(self,firstname):
            self.driver.find_element_by_id(self.firstname_textbox_name).clear()
            self.driver.find_element_by_id(self.firstname_textbox_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.lastname_textbox_name).clear()
        self.driver.find_element_by_id(self.lastname_textbox_name).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_name).clear()
        self.driver.find_element_by_id(self.email_textbox_name).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element_by_id(self.phone_number_name).clear()
        self.driver.find_element_by_id(self.phone_number_name).send_keys(phone)

    def enter_address(self, address):
        self.driver.find_element_by_id(self.address_textbox_name).clear()
        self.driver.find_element_by_id(self.address_textbox_name).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element_by_id(self.city_textbox_name).clear()
        self.driver.find_element_by_id(self.city_textbox_name).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element_by_id(self.state_textbox_name).clear()
        self.driver.find_element_by_id(self.state_textbox_name).send_keys(state)

    def enter_zip(self, zip):
        self.driver.find_element_by_id(self.zip_textbox_name).clear()
        self.driver.find_element_by_id(self.zip_textbox_name).send_keys(zip)

    def enter_website(self, website):
        self.driver.find_element_by_id(self.website_textbox_name).clear()
        self.driver.find_element_by_id(self.website_textbox_name).send_keys(website)

    def enter_description(self, description):
        self.driver.find_element_by_id(self.description_textbox_name).clear()
        self.driver.find_element_by_id(self.description_textbox_name).send_keys(description)

    def click_submit(self,submit):
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

