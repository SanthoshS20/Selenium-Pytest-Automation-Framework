from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def check_if_element_is_visible(self, locator):
        self.get_element(locator).is_displayed()

    def create_explicit_wait(self, timeout):
        return WaitDriverWait(self.driver, timeout)
    
    def wait_until_element_should_be_visible(self, locator, timeout):
        self.wait = self.create_explicit_wait(timeout)
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
    
        