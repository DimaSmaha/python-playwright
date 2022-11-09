import pytest

from pages.textbox_page import Textbox


class TestTextbox:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1280, 'height': 800})
        self.input = Textbox(self.page)
        self.page.goto('https://demoqa.com/text-box')

    def test_inputs(self, test_setup):
        self.input.fill_full_name_input("Dima")
        self.input.fill_email_input("hello@gmail.com")
        self.input.fill_current_address_input("Lviv")
        self.input.click_submit_btn()
        self.input.check_full_name_notification_shown()
        self.input.check_email_notification_shown()
        self.input.check_current_address_notification_shown()


