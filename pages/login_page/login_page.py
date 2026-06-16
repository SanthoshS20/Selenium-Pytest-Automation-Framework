from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def login(self, email_address, password):
        self.enter_text(LoginPageLocators.EMAIL_INPUT_FIELD, email_address)
        self.enter_text(LoginPageLocators.PASSWORD_INPUT_FIELD, password)
        self.click_element(LoginPageLocators.SIGN_IN_BUTTON)

    def open_url(self, base_url):
        self.navigate(base_url)
        