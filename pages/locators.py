from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    EMAIL_FIELD = (By.ID, "userEmail")
    FEMALE_GENDER_RADIO_BUTTON = (By.XPATH, "//label[@for='gender-radio-2']")
    MOBILE_FIELD = (By.ID, "userNumber")
    DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "#dateOfBirthInput")
    YEAR_SELECT = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    MONTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DAY_SELECT = (By.XPATH, "//div[@class='react-datepicker__month']//div[contains(@aria-label, '{}')]")
    SUBJECTS_FIELD = (By.ID, "subjectsInput")
    ADDRESS_FIELD = (By.ID, "currentAddress")
    STATE_SELECT_FIELD = (By.ID, "state")
    STATE_SELECT = (By.XPATH, "//div[text()='{}']")
    CITY_SELECT_FIELD = (By.ID, "city")
    CITY_SELECT = (By.XPATH, "//div[text()='{}']")
    SUBMIT_BUTTON = (By.ID, "submit")
    CHOOSE_FILE_BUTTON = (By.CSS_SELECTOR, "#uploadPicture")
    MODAL_HEADER = (By.ID, "example-modal-sizes-title-lg")
    TABLE = (By.CSS_SELECTOR, ".table-responsive")
