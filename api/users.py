from config.config_manager import ConfigManager

class Users:

    def __init__(self, api_client):
        self.api_client = api_client
        self.base_url = ConfigManager.get("api")['base_url']

    def get_users(self):
        try:
            response = self.api_client.make_api_request(method="GET", url=self.base_url + "/users")
            return response.json()
        except Exception as e:
            print(f"Error fetching users: {e}")
            return None
    
    def get_user_by_id(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        try:
            response = self.api_client.make_api_request(method="GET", url=url)
            return response.json()
        except Exception as e:
            print(f"Error fetching user by ID: {e}")
            return None
