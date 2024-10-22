from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def go_to(self):
        self.selenium_webdriver.get("https://tutorialsninja.com/demo/index.php?route=information/contact")

    def fill_contact_form(self, name, email, enquiry):
        name_field_locator = (By.NAME, "name")
        self.wait.until(EC.visibility_of_element_located(name_field_locator)).send_keys(name)

        email_field_locator = (By.NAME, "email")
        self.wait.until(EC.visibility_of_element_located(email_field_locator)).send_keys(email)

        enquiry_field_locator = (By.NAME, "enquiry")
        self.wait.until(EC.visibility_of_element_located(enquiry_field_locator)).send_keys(enquiry)

    def submit_contact_form(self):
        submit_button_locator = (By.XPATH, "//input[@value='Submit']")
        self.wait.until(EC.element_to_be_clickable(submit_button_locator)).click()

    def is_redirected_to_success_page(self):
        return self.selenium_webdriver.current_url == "https://tutorialsninja.com/demo/index.php?route=information/contact/success"
