from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def go_to(self):
        self.selenium_webdriver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
        self.selenium_webdriver.maximize_window()

    def fill_registration_form(self, firstname, lastname, email, telephone, password, confirm_password):
        self.selenium_webdriver.find_element(By.ID, "input-firstname").send_keys(firstname)
        self.selenium_webdriver.find_element(By.ID, "input-lastname").send_keys(lastname)
        self.selenium_webdriver.find_element(By.ID, "input-email").send_keys(email)
        self.selenium_webdriver.find_element(By.ID, "input-telephone").send_keys(telephone)
        self.selenium_webdriver.find_element(By.ID, "input-password").send_keys(password)
        self.selenium_webdriver.find_element(By.ID, "input-confirm").send_keys(confirm_password)

        self.selenium_webdriver.find_element(By.XPATH, "//input[@name='agree']").click()

    def submit_registration(self):
        self.selenium_webdriver.find_element(By.XPATH, "//input[@value='Continue']").click()

    def is_registration_successful(self):
        success_message_locator = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
        return self.wait.until(EC.visibility_of_element_located(success_message_locator)) is not None
