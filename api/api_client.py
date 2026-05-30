import requests
from utils.logger import Logger

class APIClient:
    def __init__(self):
        self.logger = Logger.get_logger(__name__, Logger.LOG_LEVEL)
        self.session = requests.Session()

    def make_api_request(self, method, url, params=None, json=None, data=None, headers=None, files=None, timeout=30):
        try:
            response = self.session.request(method=method, url=url, params=params, json=json, data=data, headers=headers,
                                        files=files, timeout=timeout)
            response.raise_for_status()
            logger.info(f"Request: {method} {url}")
            logger.info(f"Status Code: {response.status_code}")
            return response
        except requests.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")
