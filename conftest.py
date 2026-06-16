import pytest, allure, os
from core.driver_manager import DriverManager
from utils.screenshot_utils import ScreenshotUtils
from config.config_manager import ConfigManager
from pages.login_page.login_page import LoginPage
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")


@pytest.fixture(scope="session", autouse=True)
def initialize_config(request):
    load_dotenv()
    env = request.config.getoption("--env")
    ConfigManager.initialize(env)


@pytest.fixture(scope="class")
def setup_teardown(request):
    driver = DriverManager.get_driver(browser_name=ConfigManager.get("browser"), headless=ConfigManager.get("headless"))
    request.cls.driver = driver
    request.cls.base_url = ConfigManager.get("base_url")
    yield
    driver.quit()

@pytest.fixture(scope="class")
def authenticate_user(request):
    login_page = LoginPage(request.cls.driver)
    login_page.open_url(request.cls.base_url)
    login_page.login(
        os.getenv("TEST_EMAIL"),
        os.getenv("TEST_PASSWORD")
    )
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if hasattr(item.cls, "driver"):
            driver = item.cls.driver
            screenshot_path = ScreenshotUtils.capture(driver)
            allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)