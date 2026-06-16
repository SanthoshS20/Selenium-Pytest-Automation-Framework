from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class EventsCardLocators(BasePageLocators):

    @staticmethod
    def event_label(event_name):
        return (By.XPATH, f'//h3[text()="{event_name}"]')

    @staticmethod
    def event_price_label(event_name, event_price):
        return (By.XPATH, f'//h3[text()="{event_name}"]//ancestor::article//child::p[text()="{event_price}"]')
    
    @staticmethod
    def seats_available_label(event_name, event_price):
        return (By.XPATH, f'//h3[text()="{event_name}"]//ancestor::article//child::p[text()="{event_price}"]//following-sibling::span')
    
    @staticmethod
    def event_location_label(event_name, event_location):
        return (By.XPATH, f'//h3[text()="{event_name}"]//ancestor::article//child::span[text()="{event_location}"]')
    
    @staticmethod
    def book_now_button_for_event(event_name):
        return (By.XPATH, f'//h3[text()="{event_name}"]//ancestor::article//child::a[text()="Book Now"]')

