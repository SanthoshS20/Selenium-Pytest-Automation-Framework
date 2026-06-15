import os, constants
from utils.logger import Logger
from api.ticket_booking import TicketBooking
from utils.json_reader import JSONReader
from core.auth_manager import AuthManager
from pytest_check import check

class TestTicketBooking:

    @classmethod
    def setup_class(cls):
        cls.logger = Logger.get_logger(__name__)
        cls.logger.info("Before all - Execution started.")
        cls.client = AuthManager.authenticate(os.getenv("TEST_EMAIL"), os.getenv("TEST_PASSWORD"))
        cls.bookings_api = TicketBooking(cls.client)
        cls.bookings_data = JSONReader.read_json_data_from_file(constants.BOOKINGS_DATA_FILE_PATH)

    @classmethod
    def teardown_class(cls):
        cls.logger.info("Teardown method execution started")

    def test_create_new_bookings(self):
        self.logger.info("Test scenario - Create new booking")
        response = self.bookings_api.create_new_booking(self.bookings_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["data"]["eventId"], self.bookings_data["eventId"], "Incorrect eventId received from the response")
        check.equal(response_body["data"]["customerName"], self.bookings_data["customerName"], "Incorrect customerName received from the response")
        check.equal(response_body["data"]["customerEmail"], self.bookings_data["customerEmail"], "Incorrect customerEmail received from the response")
        check.equal(response_body["data"]["status"], "confirmed", "Incorrect status received from the response")
        check.equal(response_body["message"], "Booking confirmed!", "Booking is not confirmed")
        self.cancel_booking(response_body["data"]["id"])

    def test_get_all_bookings(self):
        self.logger.info("Test scenario - Get single booking")
        response = self.bookings_api.create_new_booking(self.bookings_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Booking confirmed!", "Booking is not confirmed")
        all_bookings_response = self.bookings_api.get_all_bookings({})
        assert all_bookings_response.status_code ==  200, f"Expected 200 but received {all_bookings_response.status_code}"
        check.equal(type(all_bookings_response.json()["data"]), list, "Its not returned all bookings")
        self.cancel_booking(response_body["data"]["id"])

    def test_single_booking(self):
        self.logger.info("Test scenario - Get single booking")
        response = self.bookings_api.create_new_booking(self.bookings_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Booking confirmed!", "Booking is not confirmed")
        get_single_booking = self.bookings_api.get_single_booking(response_body["data"]["id"])
        assert get_single_booking.status_code == 200, f"Expected 200 but received {get_single_booking.status_code}"
        check.equal(get_single_booking.json()["data"]["id"], response_body["data"]["id"], "Booking id is incorrect")
        self.cancel_booking(response_body["data"]["id"])

    def test_cancel_booking(self):
        self.logger.info("Test scenario - Cancel booking")
        response = self.bookings_api.create_new_booking(self.bookings_data)
        assert response.status_code == 201, f"Expected 201 created but received {response.status_code}"
        response_body = response.json()
        check.equal(response_body["message"], "Booking confirmed!", "Booking is not confirmed")
        booking_cancel_response = self.bookings_api.cancel_booking(response_body["data"]["id"])
        assert booking_cancel_response.status_code == 200, f"Expected 200 but received {booking_cancel_response.status_code}"
        check.equal(booking_cancel_response.json()["message"], "Booking cancelled", "Booking is not cancelled")
        all_bookings_response = self.bookings_api.get_all_bookings({})
        assert all_bookings_response.status_code ==  200, f"Expected 200 but received {all_bookings_response.status_code}"
        for booking in all_bookings_response.json()["data"]:
            check.equal(booking["id"] != response_body["data"]["id"], "Booking is not cancelled properly")


    def cancel_booking(self, booking_id):
        booking_cancel_response = self.bookings_api.cancel_booking(booking_id)
        assert booking_cancel_response.status_code == 200, f"Expected 200 but received {booking_cancel_response.status_code}"
        check.equal(booking_cancel_response.json()["message"], "Booking cancelled", "Booking is not cancelled")