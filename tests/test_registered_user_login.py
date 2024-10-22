from selenium.webdriver.common.by import By
from pages.home_page import HomePage

def test_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()

    home_page.open_login_modal()

    home_page.login(email="tupica@example.com", password="password123")

    assert home_page.is_logout_link_visible(), "Logout link is not visible, login may have failed."
