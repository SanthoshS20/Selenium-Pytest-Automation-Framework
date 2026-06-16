from pages.base_page.base_page import BasePage
from pages.events_page.events_page_locators import EventsPageLocators

class EventsPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def filter_event_with_cities(self, city_name):
        self.select_option_from_dropdown(EventsPageLocators.CITIES_DROPDOWN_FIELD, city_name)

    def search_with_title(self, event_title):
        self.enter_text(EventsPageLocators.SEARCH_EVENTS_INPUT_FIELD, event_title)

    def click_add_new_event_button(self):
        self.force_click_element(EventsPageLocators.ADD_NEW_EVENTS_BUTTON)