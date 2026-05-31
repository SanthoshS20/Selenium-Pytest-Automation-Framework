import requests
from core.api_client import APIClient
from config.config_manager import ConfigManager


class AuthManager:

    @staticmethod
    def authenticate(username, password):
        api_client = APIClient()
        try:
            response = api_client.make_api_request(
                method="POST",
                url=ConfigManager.get("auth_url"),
                json={
                    "username": username,
                    "password": password
                }
            )
            response.raise_for_status()
            return api_client
        except requests.HTTPError as http_err:
            raise requests.HTTPError(f"HTTP error occurred during authentication: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred during authentication: {err}")