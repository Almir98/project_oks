import time
from pages.home_page import HomePage

def test_slider_movement(driver):
    home_page = HomePage(driver)
    home_page.go_to()

    initial_slide_index = home_page.get_active_slide_index()

    start_time = time.time()
    timeout_duration = 20  

    while True:
        time.sleep(1)  
        current_slide_index = home_page.get_active_slide_index()
        
        if current_slide_index != initial_slide_index:
            print(f"Slider moved from {initial_slide_index} to {current_slide_index}")
            break
        
        if time.time() - start_time > timeout_duration:
            assert False, "Slider did not move to the next slide within the timeout period."

    assert True
