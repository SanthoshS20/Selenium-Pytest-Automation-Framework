import pytest, constants, allure
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--base_url", action="store")
    # parser.addoption("--env", action="store", default="test")


@pytest.fixture(scope="class")
def setup_teardown(request):
    browser_name = request.config.getoption("--browser_name")
    url = request.config.getoption("--base_url")
    # environment = request.config.getoption("--env")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.base_url = url
    # request.cls.env = environment
    yield
    driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.cls.driver

        driver.save_screenshot(constants.SCREENSHOT_PATH)

        allure.attach.file(
            constants.SCREENSHOT_PATH,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )