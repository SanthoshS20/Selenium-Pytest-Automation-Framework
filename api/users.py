from core.api_client import APIClient

class Users:

    def __init__(self):
        self.api_client = APIClient()

    def get_users(self, base_url):
        try:
            response = self.api_client.make_api_request(method="GET", url=base_url + "/users")
            return response.json()
        except Exception as e:
            print(f"Error fetching users: {e}")
            return None
    
    def get_user_by_id(self, base_url, user_id):
        url = f"{base_url}/users/{user_id}"
        try:
            response = self.api_client.make_api_request(method="GET", url=url)
            return response.json()
        except Exception as e:
            print(f"Error fetching user by ID: {e}")
            return None
