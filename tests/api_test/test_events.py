import os, constants, pytest
from utils.logger import Logger
from api.events import Events
from utils.json_reader import JSONReader
from core.auth_manager import AuthManager
from datetime import datetime, timedelta
from pytest_check import check

class TestEvemts:

    @classmethod
    def setup_class(cls):
        cls.logger = Logger.get_logger(__name__)
        cls.logger.info("Before all - Execution started.")
        cls.client = AuthManager.authenticate(os.getenv("TEST_EMAIL"), os.getenv("TEST_PASSWORD"))
        cls.events_api = Events(cls.client)
        cls.event_data = JSONReader.read_json_data_from_file(constants.EVENTS_DATA_FILE_PATH)
        cls.event_data["eventDate"] = cls.get_future_date(2)

    @classmethod
    def teardown_class(cls):
        cls.logger.info("Teardown method execution started")

    def test_create_new_events(self):
        self.logger.info("Test scenario - Create new event")
        response = self.events_api.create_new_events(self.event_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["data"]["title"], self.event_data["title"], "Incorrect title received from the response")
        check.equal(response_body["data"]["price"], str(self.event_data["price"]), "Incorrect price received from the response")
        check.equal(response_body["data"]["totalSeats"], self.event_data["totalSeats"], "Incorrect totalSeats received from the response")
        check.equal(response_body["message"], "Event created successfully", "event is not confirmed")
        self.delete_event(response_body["data"]["id"])

    def test_get_all_events(self):
        self.logger.info("Test scenario - Get single event")
        response = self.events_api.create_new_events(self.event_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Event created successfully", "event is not confirmed")
        all_events_response = self.events_api.get_all_events({})
        assert all_events_response.status_code ==  200, f"Expected 200 but received {all_events_response.status_code}"
        check.equal(type(all_events_response.json()["data"]), list, "Its not returned all events")
        self.delete_event(response_body["data"]["id"])

    def test_single_event(self):
        self.logger.info("Test scenario - Get single event")
        response = self.events_api.create_new_events(self.event_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Event created successfully", "event is not confirmed")
        get_single_event = self.events_api.get_single_event(response_body["data"]["id"])
        assert get_single_event.status_code == 200, f"Expected 200 but received {get_single_event.status_code}"
        check.equal(get_single_event.json()["data"]["id"], response_body["data"]["id"], "event id is incorrect")
        self.delete_event(response_body["data"]["id"])

    def test_delete_event(self):
        self.logger.info("Test scenario - Cancel event")
        response = self.events_api.create_new_events(self.event_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Event created successfully", "event is not confirmed")
        self.delete_event(response_body["data"]["id"])
        all_events_response = self.events_api.get_all_events({})
        assert all_events_response.status_code ==  200, f"Expected 200 but received {all_events_response.status_code}"
        for event in all_events_response.json()["data"]:
            check.not_equal(event["id"], response_body["data"]["id"], "event is not cancelled properly")


    def test_update_event(self):
        self.logger.info("Test scenario - Update event")
        response = self.events_api.create_new_events(self.event_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Event created successfully", "event is not confirmed")
        self.event_data["title"] = "welcome"
        update_response = self.events_api.update_event(response_body["data"]["id"], self.event_data)
        assert update_response.status_code == 200, "Event is not updated"
        check.equal(update_response.json()["data"]["title"], "welcome", "Title is not updated")
        self.delete_event(response_body["data"]["id"])

    def delete_event(self, event_id):
        event_delete_response = self.events_api.delete_event(event_id)
        assert event_delete_response.status_code == 200, f"Expected 200 but received {event_delete_response.status_code}"
        check.equal(event_delete_response.json()["message"], "Event deleted successfully", "event is not deleted")

    def get_future_date(self, days=1):
        return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S")