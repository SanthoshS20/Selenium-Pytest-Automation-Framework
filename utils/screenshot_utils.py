import os, constants
from datetime import datetime

class ScreenshotUtils:

    @staticmethod
    def capture(driver):
        os.makedirs("screenshots", exist_ok=True)
        screenshot_dir = os.path.join(constants.BASE_DIR, 'screenshots')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_path = os.path.join(
            screenshot_dir,
            f"screenshot_{timestamp}.png"
        )
        driver.save_screenshot(screenshot_path)

        return screenshot_path