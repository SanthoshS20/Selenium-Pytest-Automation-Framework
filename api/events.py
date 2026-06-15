from config.config_manager import ConfigManager

class Events:

    def __init__(self, api_client):
        self.api_client = api_client
        self.base_url = ConfigManager.get("api")['base_url']

    def create_new_events(self, event_info):
        self.new_event_response = self.api_client.make_api_request(method='POST', url=self.base_url + '/events', json=event_info)
        return self.new_event_response
    
    def get_all_events(self, event_params):
        self.all_events_response = self.api_client.make_api_request(method='GET', url=self.base_url + '/events', params=event_params)
        return self.all_events_response
    
    def get_single_event(self, event_id):
        self.single_event_response = self.api_client.make_api_request(method='GET', url=self.base_url + '/events/' + str(event_id))
        return self.single_event_response
    
    def delete_event(self, event_id):
        self.delete_event_response = self.api_client.make_api_request(method='DELETE', url=self.base_url + '/events/' + str(event_id))
        return self.delete_event_response 
    
    def update_event(self, event_id, event_info):
        self.updated_event_response = self.api_client.make_api_request(method='PUT', url=self.base_url + '/events/' + str(event_id), json=event_info)
        return self.updated_event_response
 

