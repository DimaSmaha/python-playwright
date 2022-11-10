import string

from playwright.sync_api import Page, expect


class DynamicProperties:

    def __init__(self, page: Page):
        # double underscore for locators be private

        self.page = page
        self.__enable_in_5_seconds_btn = self.page.locator('[id="enableAfter"]')
        self.__visible_after_5_seconds_btn = self.page.locator('[id="visibleAfter"]')

    def check_button_enable_in_5_seconds(self) -> None:
        self.__enable_in_5_seconds_btn.wait_for(state='visible')
        expect(self.__enable_in_5_seconds_btn).to_be_enabled(timeout=6000)

    def check_button_visible_in_5_seconds(self) -> None:
        self.__visible_after_5_seconds_btn.wait_for(state='visible')
        expect(self.__visible_after_5_seconds_btn).to_be_visible()
