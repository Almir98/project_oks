import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    selenium_driver = webdriver.Chrome(service=service)
    yield selenium_driver
    selenium_driver.quit()
    