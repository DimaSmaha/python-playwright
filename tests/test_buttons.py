import pytest

from pages.buttons_page import Buttons


class TestButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1280, 'height': 800})
        self.buttons = Buttons(self.page)
        self.page.goto('https://demoqa.com/buttons')

    def test_double_click_button(self, test_setup):
        """Test to verify the functionality of the double click button
        :param test_setup: setting up the browser and page objects
        :return: None
        """
        self.buttons.click_double_click_btn()
        self.buttons.check_double_click_notification_shown()

    def test_rmb_click_button(self, test_setup):
        """Test to verify the functionality of the Right Mouse Button click button
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.click_right_click_btn()
        self.buttons.check_right_click_notification_shown()

    def test_dynamic_button(self, test_setup):
        """Test to verify the functionality of the dynamic button
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.clickBtn()
        self.buttons.check_dynamic_click_notification_shown()

    def test_buttons(self, test_setup):
        """Test to verify the functionality of the double click button, Right Mouse Button click button and
        dynamic button
        :param test_setup:
        :return: None
        """
        self.buttons.click_double_click_btn()
        self.buttons.check_double_click_notification_shown()

        self.buttons.click_right_click_btn()
        self.buttons.check_right_click_notification_shown()

        self.buttons.clickBtn()
        self.buttons.check_dynamic_click_notification_shown()
