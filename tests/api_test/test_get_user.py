from utils.logger import Logger
from api.users import Users
from config.config_manager import ConfigManager
from core.auth_manager import AuthManager


class TestGetUser:

    def setup_method(self, method):
        print("Setup method for TestGetUser")
        self.client = AuthManager.authenticate("admin", "admin123")
        self.logger = Logger.get_logger(__name__)
        self.users_api = Users(self.client)
        print("ConfigManager._config in setup_method:", ConfigManager._config)

    def test_get_all_users(self):
        self.logger.info("Testing: Get all users")
        response = self.users_api.get_users()
        assert isinstance(response, list), "Expected a list of users"
        assert len(response) > 0, "Expected at least one user in the response"

    def test_get_user_by_id(self):
        self.logger.info("Testing: Get user by ID")
        user_id = 1
        response = self.users_api.get_user_by_id(user_id)
        assert isinstance(response, dict), "Expected a dictionary for user details"
        assert response.get("id") == user_id, f"Expected user ID to be {user_id}"