from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class LoginPageLocators(BasePageLocators):

    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@id="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="password"]')
    REGISTER_LINK = (By.XPATH, '//a[text()="Register"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@id="login-btn"]')
