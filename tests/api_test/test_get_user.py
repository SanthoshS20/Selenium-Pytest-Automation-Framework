from utils.logger import Logger
from api.users import Users
from config.config_manager import ConfigManager


class TestGetUser:

    def setup_method(self, method):
        print("Setup method for TestGetUser")
        self.logger = Logger.get_logger(__name__)
        self.users_api = Users()
        print("ConfigManager._config in setup_method:", ConfigManager._config)
        self.base_url = ConfigManager.get("api")["base_url"]

    def test_get_all_users(self):
        self.logger.info("Testing: Get all users")
        response = self.users_api.get_users(self.base_url)
        assert isinstance(response, list), "Expected a list of users"
        assert len(response) > 0, "Expected at least one user in the response"

    def test_get_user_by_id(self):
        self.logger.info("Testing: Get user by ID")
        user_id = 1
        response = self.users_api.get_user_by_id(self.base_url, user_id)
        assert isinstance(response, dict), "Expected a dictionary for user details"
        assert response.get("id") == user_id, f"Expected user ID to be {user_id}"