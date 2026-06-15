import requests
from core.api_client import APIClient
from utils.logger import Logger
from config.config_manager import ConfigManager


class AuthManager:

    @staticmethod
    def authenticate(email, password):
        api_client = APIClient()
        logger = Logger.get_logger(__name__)
        try:
            response = api_client.make_api_request(
                method="POST",
                url=ConfigManager.get("api")["base_url"] + "/auth/login",
                json={
                    "email": email,
                    "password": password
                }
            )
            response.raise_for_status()
            api_client.update_headers({
                "Authorization": f"Bearer {response.json()['token']}"
            })
            logger.info(f"Log-in successful for the {email}")
            return api_client
        except requests.HTTPError as http_err:
            raise requests.HTTPError(f"HTTP error occurred during authentication: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred during authentication: {err}")