from pages.base_page.base_page import BasePage
from components.navbar.navbar_locators import NavbarLocators

class Navbar(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def click_events_navbar(self):
        self.click_element(NavbarLocators.events_nav_link())

    