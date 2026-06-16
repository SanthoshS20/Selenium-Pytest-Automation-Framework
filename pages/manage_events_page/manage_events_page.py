from pages.base_page.base_page import BasePage
from pages.manage_events_page.manage_events_page_locators import ManageEventsPageLocators

class ManageEventsPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def create_new_event(self, event_data):
        self.enter_text(ManageEventsPageLocators.EVENT_TITLE_INPUT_FIELD, event_data.get('title'))
        self.enter_text(ManageEventsPageLocators.CITY_INPUT_FIELD, event_data.get('city'))
        self.enter_text(ManageEventsPageLocators.VENUE_INPUT_FIELD, event_data.get('venue'))
        self.enter_text(ManageEventsPageLocators.PRICE_INPUT_FIELD, event_data.get('price'))
        self.enter_text(ManageEventsPageLocators.TOTAL_SEATS_INPUT_FIELD, event_data.get('totalSeats'))
        self.select_event_datetime(event_data.get('eventDate'))
        self.click_element(ManageEventsPageLocators.ADD_EVENT_BUTTON)
        self.wait_until_element_should_be_visible(ManageEventsPageLocators.EVENT_CREATED_MESSAGE)
        
    def select_event_datetime(self, datetime):
        date, time = datetime.split("T")
        self.enter_text(ManageEventsPageLocators.EVENT_DATETIME_INPUT_FIELD, date)
        self.click_tab()
        self.enter_text(ManageEventsPageLocators.EVENT_DATETIME_INPUT_FIELD, time)