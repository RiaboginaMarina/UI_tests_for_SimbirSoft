import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def registration_test_data():
    return {
        "date_of_birth": {
            "day": "9",
            "month": "March",
            "year": "1999",
        },
        "name": "Марина",
        "surname": "Рябогина",
        "email": "mryabogina@gmail.com",
        "mobile_number": "9522712187",
        "subjects": "Я люблю автоматизировать тесты",
        "address": "ул. А.Петрова, д.178",
        "picture": "good_boy.jpg",
        "city": "Delhi",
        "state": "NCR",
        "gender": "Female",
    }
