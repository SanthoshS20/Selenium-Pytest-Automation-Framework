import pytest
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
    request.cls.driver = driver
    request.cls.base_url = url
    # request.cls.env = environment
    yield
    driver.quit()
