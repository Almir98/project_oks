from pages.home_page import HomePage

def test_footer_visibility(driver):
    home_page = HomePage(driver)
    home_page.go_to()

    assert home_page.is_footer_visible() == True, "Footer is not visible on the page"
