from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, selenium_webdriver):
        self.selenium_webdriver = selenium_webdriver
        self.wait = WebDriverWait(selenium_webdriver, timeout=60)

    def go_to(self):
        self.selenium_webdriver.get("https://tutorialsninja.com/demo/")
        self.selenium_webdriver.maximize_window()

    def get_page_title(self):
        return self.selenium_webdriver.title

    def open_login_modal(self):
        account_link_locator = (By.XPATH, "//span[text()='My Account']")
        self.wait.until(EC.element_to_be_clickable(account_link_locator)).click()

        login_button_locator = (By.XPATH, "//a[text()='Login']")
        self.wait.until(EC.element_to_be_clickable(login_button_locator)).click()

    def login(self, email, password):
        email_field_locator = (By.ID, "input-email")
        self.wait.until(EC.element_to_be_clickable(email_field_locator)).send_keys(email)

        password_field_locator = (By.ID, "input-password")
        self.wait.until(EC.element_to_be_clickable(password_field_locator)).send_keys(password)

        login_button_locator = (By.XPATH, "//input[@value='Login']")
        self.selenium_webdriver.find_element(*login_button_locator).click()

    def is_alert_present(self):
        try:
            self.wait.until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def get_login_error_message(self):
        error_message_locator = (By.XPATH, "//div[contains(@class, 'alert-danger')]")
        return self.wait.until(EC.visibility_of_element_located(error_message_locator)).text

    def is_logout_link_visible(self):
        account_link_locator = (By.XPATH, "//span[text()='My Account']")
        self.wait.until(EC.element_to_be_clickable(account_link_locator)).click()
        logout_link_locator = (By.XPATH, "//a[text()='Logout']")
        return self.wait.until(EC.visibility_of_element_located(logout_link_locator)).is_displayed()

    def is_search_bar_visible(self):
        search_bar_locator = (By.NAME, "search")
        try:
            search_bar = self.wait.until(EC.visibility_of_element_located(search_bar_locator))
            return search_bar.is_displayed()
        except TimeoutException:
            return False

    def is_cart_icon_visible(self):
        cart_icon_locator = (By.ID, "cart")
        try:
            cart_icon = self.wait.until(EC.visibility_of_element_located(cart_icon_locator))
            return cart_icon.is_displayed()
        except TimeoutException:
            return False
        
    def is_footer_visible(self):
        footer_locator = (By.TAG_NAME, "footer")  
        try:
            footer = self.wait.until(EC.visibility_of_element_located(footer_locator))
            return footer.is_displayed()
        except TimeoutException:
            return False    
        
    def get_active_slide_index(self):
        active_slide_locator = (By.CSS_SELECTOR, ".swiper-slide-active")
        active_slide = self.wait.until(EC.visibility_of_element_located(active_slide_locator))
        return active_slide.get_attribute("data-swiper-slide-index")    
    
    def search_for_product(self, search_term):
        search_box_locator = (By.NAME, "search")
        self.wait.until(EC.visibility_of_element_located(search_box_locator)).send_keys(search_term)

        search_button_locator = (By.XPATH, "//button[@type='button' and @class='btn btn-default btn-lg']")
        self.wait.until(EC.element_to_be_clickable(search_button_locator)).click()

    def add_product_to_wishlist(self, product_name):
        product_locator = (By.LINK_TEXT, product_name)
        product_element = self.wait.until(EC.visibility_of_element_located(product_locator))
        product_element.click()

        add_to_wishlist_locator = (By.XPATH, "//button[@data-original-title='Add to Wish List']")
        self.wait.until(EC.element_to_be_clickable(add_to_wishlist_locator)).click()
        