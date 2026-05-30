from pages.base_page.base_page import BasePage
from pages.form_page.form_page_locators import FormPageLocators
import time


class FormPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.enter_text(FormPageLocators.FIRST_NAME_INPUT_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(FormPageLocators.LAST_NAME_INPUT_FIELD, last_name)

    def select_gender(self, gender):
        if gender == 'M':
            self.click_element(FormPageLocators.MALE_RADIO_BUTTON)
        elif gender == 'F':
            self.click_element(FormPageLocators.FEMALE_RADIO_BUTTON)
    
    def enter_mobile_number(self, number):
        self.enter_text(FormPageLocators.MOBILE_NUMBER_INPUT_FIELD, number)

    def click_submit_button(self):
        self.scroll_to_element(FormPageLocators.SUBMIT_BUTTON)
        self.force_click_element(FormPageLocators.SUBMIT_BUTTON)

    def check_if_form_submit_confirm_message_displayed(self):
        self.wait_until_element_should_be_visible(FormPageLocators.FORM_SUBMIT_CONFIRM_MESSAGE)
        return self.check_if_element_is_visible(FormPageLocators.FORM_SUBMIT_CONFIRM_MESSAGE)
        