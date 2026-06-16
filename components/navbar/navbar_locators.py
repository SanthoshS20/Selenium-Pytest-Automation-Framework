from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class NavbarLocators(BasePageLocators):

    @staticmethod
    def events_nav_link():
        return (By.XPATH, '//a[@href="/events" and text()="Events"]')

