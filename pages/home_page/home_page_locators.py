from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class HomePageLocators(BasePageLocators):

    EVENTS_HEADER_CONTENT = (By.XPATH, '//span[text()="Amazing Events"]')
    BROWSE_EVENTS_BUTTON = (By.XPATH, '//span[contains(text(), "Browse Events")]')
    MY_BOOKINGS_BUTTON = (By.XPATH, '//button[text()="My Bookings"]')
