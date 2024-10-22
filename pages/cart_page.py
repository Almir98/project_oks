from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def is_empty_cart_message_displayed(self):
        empty_cart_message_locator = (By.XPATH, "//*[@id='content']/p[contains(text(), 'Your shopping cart is empty!')]")
        try:
            return self.wait.until(EC.visibility_of_element_located(empty_cart_message_locator)).is_displayed()
        except TimeoutException:
            return False  
