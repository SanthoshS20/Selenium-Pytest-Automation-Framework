from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverManager:

    @staticmethod
    def get_driver(browser_name="chrome", headless=False):

        if browser_name.lower() == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False
            }

            options.add_experimental_option("prefs", prefs)

            options.add_argument("--disable-features=PasswordLeakDetection")
            options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        else:
            raise Exception(f"Unsupported browser: {browser_name}")
        return driver