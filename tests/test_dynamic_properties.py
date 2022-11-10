import pytest

from pages.dynamic_prop_page import DynamicProperties


class TestTextbox:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1280, 'height': 800})
        self.dynamic_prop = DynamicProperties(self.page)
        self.page.goto('https://demoqa.com/dynamic-properties')

    def test_dynamic_properties(self, test_setup):
        self.dynamic_prop.check_button_enable_in_5_seconds()
        self.dynamic_prop.check_button_visible_in_5_seconds()


