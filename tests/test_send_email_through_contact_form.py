from pages.contact_page import ContactPage

def test_send_email_through_contact_form(driver):
    contact_page = ContactPage(driver)

    contact_page.go_to()

    contact_page.fill_contact_form(
        name="Test User",
        email="testuser@example.com",  
        enquiry="This is a test enquiry message."
    )

    contact_page.submit_contact_form()

    assert contact_page.is_redirected_to_success_page(), \
        "The user was not redirected to the success page after submitting the contact form."
