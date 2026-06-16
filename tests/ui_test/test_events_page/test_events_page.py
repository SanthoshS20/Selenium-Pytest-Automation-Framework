from core.auth_manager import AuthManager
from pages.login_page.login_page import LoginPage
from pages.events_page.events_page import EventsPage
from pages.home_page.home_page import HomePage
from pages.manage_events_page.manage_events_page import ManageEventsPage
from components.events_card.events_card import EventsCard
from components.navbar.navbar import Navbar
import pytest, constants, os
from api.events import Events
from utils.logger import Logger
from utils.json_reader import JSONReader
from datetime import datetime, timedelta


@pytest.fixture(scope="class")
def initialization(request):
    request.cls.logger = Logger.get_logger(__name__)
    request.cls.home_page = HomePage(request.cls.driver)
    request.cls.manage_events_page = ManageEventsPage(request.cls.driver)
    request.cls.events_page = EventsPage(request.cls.driver)
    request.cls.navbar = Navbar(request.cls.driver)
    request.cls.events_api = Events(request.cls.driver)
    request.cls.client = AuthManager.authenticate(os.getenv("TEST_EMAIL"), os.getenv("TEST_PASSWORD"))
    request.cls.events_api = Events(request.cls.client)
    request.cls.events_card = EventsCard(request.cls.driver)
    request.cls.events_data = JSONReader.read_json_data_from_file(constants.EVENTS_DATA_FILE_PATH)

def teardown_method(self, method):
    self.events_api.delete_event()

@pytest.mark.usefixtures("setup_teardown", "authenticate_user", "initialization")
class TestEvents:

    def test_create_new_event(self):
        self.navbar.click_events_navbar()
        self.events_page.click_add_new_event_button()
        self.events_data["eventDate"] = (datetime.now() + timedelta(days=2)).strftime("%d-%m-%YT%H-%M")
        self.manage_events_page.create_new_event(self.events_data)
        self.navbar.click_events_navbar()
        self.events_card.check_event_is_present(self.events_data.get('title'))


    def test_create_new_event1(self):
        self.navbar.click_events_navbar()
        self.events_page.click_add_new_event_button()
        self.events_data["title"] = "powerful"
        self.events_data["eventDate"] = (datetime.now() + timedelta(days=2)).strftime("%d-%m-%YT%H-%M")
        self.manage_events_page.create_new_event(self.events_data)
        self.navbar.click_events_navbar()
        self.events_card.check_event_is_present(self.events_data.get('title'))