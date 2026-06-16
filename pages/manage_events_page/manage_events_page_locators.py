from pages.base_page.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By

class ManageEventsPageLocators(BasePageLocators):

    EVENT_TITLE_INPUT_FIELD = (By.XPATH, '//input[@id="event-title-input"]')
    CITY_INPUT_FIELD = (By.XPATH, '//input[@id="city"]')
    VENUE_INPUT_FIELD = (By.XPATH, '//input[@id="venue"]')
    EVENT_DATETIME_INPUT_FIELD = (By.XPATH, '//input[@id="event-date-&-time"]')
    PRICE_INPUT_FIELD = (By.XPATH, '//input[@id="price-($)"]')
    TOTAL_SEATS_INPUT_FIELD = (By.XPATH, '//input[@id="total-seats"]')
    ADD_EVENT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    EVENT_CREATED_MESSAGE = (By.XPATH, '//p[text()="Event created!"]')