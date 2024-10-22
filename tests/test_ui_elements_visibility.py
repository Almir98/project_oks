from pages.home_page import HomePage

def test_ui_elements_visibility(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    assert home_page.is_search_bar_visible() == True
    assert home_page.is_cart_icon_visible() == True
