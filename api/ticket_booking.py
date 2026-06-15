from config.config_manager import ConfigManager

class TicketBooking:

    def __init__(self, api_client):
        self.api_client = api_client
        self.base_url = ConfigManager.get("api")['base_url']

    def create_new_booking(self, booking_info):
        self.new_booking_response = self.api_client.make_api_request(method='POST', url=self.base_url + '/bookings', json=booking_info)
        return self.new_booking_response
    
    def get_all_bookings(self, booking_params):
        self.all_bookings = self.api_client.make_api_request(method='GET', url=self.base_url + '/bookings', params=booking_params)
        return self.all_bookings
    
    def get_single_booking(self, booking_id):
        self.single_bookings = self.api_client.make_api_request(method='GET', url=self.base_url + '/bookings/' + str(booking_id))
        return self.single_bookings
    
    def cancel_booking(self, booking_id):
        self.single_bookings = self.api_client.make_api_request(method='DELETE', url=self.base_url + '/bookings/' + str(booking_id))
        return self.single_bookings 
    
    def clear_all_booking(self):
        self.clear_bookings = self.api_client.make_api_request(method='DELETE', url=self.base_url + '/bookings/')
        return self.clear_bookings
 

