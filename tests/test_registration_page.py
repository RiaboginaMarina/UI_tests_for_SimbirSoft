from pages.registration_page import RegistrationPage


def test_registration_results_window_header_text(browser, registration_test_data):
    page = RegistrationPage(browser)
    page.open()
    page.fill_registration_form(registration_test_data)
    page.click_submit_button()
    expected_modal_window_header_text = "Thanks for submitting the form"
    actual_modal_window_header_text = page.get_text_from_modal_window_header()
    assert expected_modal_window_header_text == actual_modal_window_header_text, "Нет заголовка с текстом 'Thanks for submitting the form'"


def test_registration_results_window_content(browser, registration_test_data):
    page = RegistrationPage(browser)
    page.open()
    page.fill_registration_form(registration_test_data)
    page.click_submit_button()
    user_data = page.get_table_data()
    assert user_data == registration_test_data, "Данные в таблице не соответствуют введенным значениям"
