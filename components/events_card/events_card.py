from pages.base_page.base_page import BasePage
from components.events_card.events_card_locators import EventsCardLocators

class EventsCard(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def click_book_now_button(self, event_name):
        self.click_element(EventsCardLocators.book_now_button_for_event(event_name))

    def check_event_is_present(self, event_name):
        self.check_if_element_is_visible(EventsCardLocators.event_label(event_name))
    