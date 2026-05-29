from selenium.webdriver.common.by import By
from pages.base_page.base_page_locators import BasePageLocators


class FormPageLocators(BasePageLocators):

    FIRST_NAME_INPUT_FIELD = (By.ID, 'firstName')
    LAST_NAME_INPUT_FIELD = (By.ID, 'lastName')
    MALE_RADIO_BUTTON = (By.XPATH , '//input[@id="gender_0"]')
    FEMALE_RADIO_BUTTON = (By.XPATH , '//input[@id="gender_1"]')
    MOBILE_NUMBER_INPUT_FIELD = (By.NAME, 'mobile')
    SUBMIT_BUTTON = (By.XPATH, '//input[@value="Submit"]')
    FORM_SUBMIT_CONFIRM_MESSAGE = (By.XPATH, '//h5[text()="Thanks for submitting the form"]')