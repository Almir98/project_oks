from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WelcomePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def is_login_link_invisible(self):
        login_link_locator = (By.XPATH, "//a[text()='Login']")
        return self.wait.until(EC.invisibility_of_element_located(login_link_locator))

    def is_signup_link_invisible(self):
        signup_link_locator = (By.XPATH, "//a[text()='Register']")
        return self.wait.until(EC.invisibility_of_element_located(signup_link_locator))

    def is_logout_link_visible(self):
        logout_link_locator = (By.XPATH, "//a[text()='Logout']")
        return self.wait.until(EC.visibility_of_element_located(logout_link_locator))

    def get_welcome_text(self):
        welcome_text_locator = (By.XPATH, "//a[text()='My Account']")
        return self.wait.until(EC.visibility_of_element_located(welcome_text_locator)).text
