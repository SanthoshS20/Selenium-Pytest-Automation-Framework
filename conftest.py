import pytest, constants, allure
from selenium import webdriver
from core.driver_manager import DriverManager
from utils.screenshot_utils import ScreenshotUtils


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--base_url", action="store")


@pytest.fixture(scope="class")
def setup_teardown(request):
    browser_name = request.config.getoption("--browser_name")
    url = request.config.getoption("--base_url")
    driver = DriverManager.get_driver(browser_name=browser_name)
    request.cls.driver = driver
    request.cls.base_url = url
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