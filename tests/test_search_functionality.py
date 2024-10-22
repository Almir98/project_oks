from selenium.webdriver.common.by import By  
from pages.home_page import HomePage

def test_search_functionality(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    
    search_term = "iPhone"
    home_page.search_for_product(search_term)

    assert driver.current_url == f"https://tutorialsninja.com/demo/index.php?route=product/search&search={search_term}", \
        f"Expected to be on '{f'https://tutorialsninja.com/demo/index.php?route=product/search&search={search_term}'}', but got {driver.current_url} instead"

    product_thumb_locator = (By.CLASS_NAME, "product-thumb")
    results = driver.find_elements(*product_thumb_locator)
    
    assert len(results) > 0, f"Expected at least 1 product result, but got {len(results)} instead."
