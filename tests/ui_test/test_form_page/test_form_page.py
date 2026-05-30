from utils.logger import Logger
import pytest, constants
from pages.form_page.form_page import FormPage

@pytest.mark.usefixtures("setup_teardown")
class TestFormPage:

    def setup_method(self, method):
        self.log = Logger.get_logger(__name__, constants.LOG_LEVEL)
        self.form_page = FormPage(self.driver)
        self.log.info("Test setup completed.")
        self.form_page.open_url(self.base_url)


    def test_submit_form_with_valid_values(self):
        self.form_page.enter_first_name("ram")
        self.form_page.enter_last_name("suresh")
        self.form_page.select_gender('F')
        self.form_page.enter_mobile_number('1234567890')
        self.form_page.click_submit_button()
        assert self.form_page.check_if_form_submit_confirm_message_displayed(), "Form submit confirmation message is not displayed."
        