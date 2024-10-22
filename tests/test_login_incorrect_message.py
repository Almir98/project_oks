from pages.home_page import HomePage
from pages.welcome_page import WelcomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    
    home_page.go_to()
    assert home_page.get_page_title() == "Your Store"
    
    home_page.open_login_modal()
    home_page.login("test@example.com", "password123")  
    
    error_message = home_page.get_login_error_message()
    assert "Warning: No match for E-Mail Address and/or Password." in error_message