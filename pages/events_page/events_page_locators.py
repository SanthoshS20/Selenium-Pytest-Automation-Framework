from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By


class EventsPageLocators(BasePageLocators):

    SEARCH_EVENTS_INPUT_FIELD = (By.XPATH, '//input[@placeholder="Search events, venues…"]')
    CATEGORIES_DROPDOWN_FIELD = (By.XPATH, '//option[text()="All Categories"]//parent::select')
    CITIES_DROPDOWN_FIELD = (By.XPATH, '//option[text()="All Cities"]//parent::select')
    ADD_NEW_EVENTS_BUTTON = (By.XPATH, '//button[text()="Add New Event"]')



    
    