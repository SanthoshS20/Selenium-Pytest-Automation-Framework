from pages.base_page.base_page import BasePage
from pages.home_page.home_page_locators import HomePageLocators

class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def verify_page_elements(self):
        self.check_if_element_is_visible(HomePageLocators.EVENTS_HEADER_CONTENT)
        self.check_if_element_is_visible(HomePageLocators.MY_BOOKINGS_BUTTON)
        self.check_if_element_is_visible(HomePageLocators.BROWSE_EVENTS_BUTTON)

    def click_browse_events_button(self):
        self.click_element(HomePageLocators.BROWSE_EVENTS_BUTTON)

