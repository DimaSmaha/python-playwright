import pytest

from pages.checkbox_page import Checkbox


class TestCheckbox:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1280, 'height': 800})
        self.chb = Checkbox(self.page)
        self.page.goto('https://demoqa.com/checkbox')

    def test_chb(self, test_setup):
        self.chb.click_home_chb()
        self.chb.check_success_notification_shown()
