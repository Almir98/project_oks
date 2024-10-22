from pages.cart_page import CartPage

def test_empty_cart_message(driver):
    driver.get("https://tutorialsninja.com/demo/index.php?route=checkout/cart")
    driver.maximize_window()  

    cart_page = CartPage(driver)
    
    assert cart_page.is_empty_cart_message_displayed()  
