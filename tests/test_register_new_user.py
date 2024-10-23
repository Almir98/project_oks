from pages.register_page import RegisterPage

def test_register_and_login(driver):
    register_page = RegisterPage(driver)
    register_page.go_to()

    register_page.fill_registration_form(
        firstname="Test", 
        lastname="User", 
        email="almir1234@example.com", 
        telephone="123456789", 
        password="password123", 
        confirm_password="password123"
    )
    
    register_page.submit_registration()

    assert driver.current_url != "https://tutorialsninja.com/demo/index.php?route=account/register", \
        f"Expected to be redirected to another page, but still on 'https://tutorialsninja.com/demo/index.php?route=account/register'"