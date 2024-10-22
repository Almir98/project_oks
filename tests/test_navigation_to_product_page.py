from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_navigation_to_product_page(driver):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    home_page.go_to()

    product_link = home_page.selenium_webdriver.find_element(By.LINK_TEXT, "Canon EOS 5D")
    product_link.click()

    assert product_page.is_product_displayed("Canon EOS 5D"), "The product 'Canon EOS 5D' is not displayed on the page."
