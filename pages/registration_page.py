import os
from datetime import datetime as dt

import pandas as pd
from selenium.webdriver.support.ui import Select

from pages.locators import RegistrationPageLocators


class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://demoqa.com/automation-practice-form'

    def open(self):
        self.browser.get(self.url)

    def set_name(self, name):
        name_field = self.browser.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD)
        name_field.send_keys(name)

    def set_surname(self, surname):
        surname_field = self.browser.find_element(*RegistrationPageLocators.LAST_NAME_FIELD)
        surname_field.send_keys(surname)

    def set_email(self, email):
        email_field = self.browser.find_element(*RegistrationPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def set_mobile_number(self, mobile_number):
        mobile_number_field = self.browser.find_element(*RegistrationPageLocators.MOBILE_FIELD)
        mobile_number_field.send_keys(mobile_number)

    def set_subjects(self, text):
        subjects_field = self.browser.find_element(*RegistrationPageLocators.SUBJECTS_FIELD)
        subjects_field.send_keys(text)

    def set_address(self, address):
        address_field = self.browser.find_element(*RegistrationPageLocators.ADDRESS_FIELD)
        address_field.send_keys(address)

    def choose_female_gender(self):
        self.browser.find_element(*RegistrationPageLocators.FEMALE_GENDER_RADIO_BUTTON).click()

    def select_state(self, state_name):
        state_field = self.browser.find_element(*RegistrationPageLocators.STATE_SELECT_FIELD)
        state_field.click()
        state = self.browser.find_element(
            RegistrationPageLocators.STATE_SELECT[0],
            RegistrationPageLocators.STATE_SELECT[1].format(state_name)
        )
        state.click()

    def select_city(self, city_name):
        city_field = self.browser.find_element(*RegistrationPageLocators.CITY_SELECT_FIELD)
        city_field.click()
        city = self.browser.find_element(
            RegistrationPageLocators.CITY_SELECT[0],
            RegistrationPageLocators.CITY_SELECT[1].format(city_name)
        )
        city.click()

    def load_image(self, image):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, image)
        choose_file_button = self.browser.find_element(*RegistrationPageLocators.CHOOSE_FILE_BUTTON)
        choose_file_button.send_keys(file_path)

    def select_date_of_birth(self, date_of_birth):
        date_of_birth_field = self.browser.find_element(*RegistrationPageLocators.DATE_OF_BIRTH_FIELD)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", date_of_birth_field)
        date_of_birth_field.click()
        month_select = Select(self.browser.find_element(*RegistrationPageLocators.MONTH_SELECT))
        month_select.select_by_visible_text(date_of_birth["month"])
        year_select = Select(self.browser.find_element(*RegistrationPageLocators.YEAR_SELECT))
        year_select.select_by_value(date_of_birth["year"])
        day_select = self.browser.find_element(
            RegistrationPageLocators.DAY_SELECT[0],
            RegistrationPageLocators.DAY_SELECT[1].format(f'{date_of_birth["month"]} {date_of_birth["day"]}')
        )
        day_select.click()

    def fill_registration_form(self, registration_test_data):
        self.set_name(registration_test_data["name"])
        self.set_surname(registration_test_data["surname"])
        self.set_email(registration_test_data["email"])
        self.choose_female_gender()
        self.set_mobile_number(registration_test_data["mobile_number"])
        self.select_date_of_birth(registration_test_data["date_of_birth"])
        self.set_subjects(registration_test_data["subjects"])
        self.load_image(registration_test_data["picture"])
        self.set_address(registration_test_data["address"])
        self.select_state(registration_test_data["state"])
        self.select_city(registration_test_data["city"])

    def click_submit_button(self):
        self.browser.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def get_text_from_modal_window_header(self):
        header = self.browser.find_element(*RegistrationPageLocators.MODAL_HEADER)
        header_text = header.text
        return header_text

    def get_table_data(self):
        table = self.browser.find_element(*RegistrationPageLocators.TABLE)
        table_html = table.get_attribute("innerHTML")
        df = pd.read_html(table_html)
        data = {"date_of_birth": {}}
        for key, value in df[0].values:
            if key == 'Student Name':
                name, surname = value.split()
                data["name"] = name
                data["surname"] = surname
            if key == 'Student Email':
                data["email"] = value
            if key == 'Mobile':
                data["mobile_number"] = value
            if key == 'State and City':
                state, city = value.split()
                data["state"] = state
                data["city"] = city
            if key == 'Date of Birth':
                date = dt.strptime(value, '%d %B,%Y')
                data["date_of_birth"]["day"] = str(date.day)
                data["date_of_birth"]["month"] = date.strftime("%B")
                data["date_of_birth"]["year"] = str(date.year)
            if key == "Gender":
                data["gender"] = value
            if key == "Subjects":
                data["subjects"] = value
            if key == "Picture":
                data["picture"] = value
            if key == "Address":
                data["address"] = value
        return data
