import pytest, constants, allure
from selenium import webdriver
from core.driver_manager import DriverManager
from utils.screenshot_utils import ScreenshotUtils
from config.config_manager import ConfigManager


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")


@pytest.fixture(scope="class")
def setup_teardown(request):
    ConfigManager.initialize(request.config.getoption("--env"))
    driver = DriverManager.get_driver(browser_name=ConfigManager.get("browser"), headless=ConfigManager.get("headless"))
    request.cls.driver = driver
    request.cls.base_url = ConfigManager.get("base_url")
    yield
    driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.cls.driver

        screenshot_path = ScreenshotUtils.capture(driver)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )