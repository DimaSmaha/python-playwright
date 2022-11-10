import string

from playwright.sync_api import Page, expect


class Checkbox:

    def __init__(self, page: Page):
        # double underscore for locators be private

        self.page = page
        self.__home_checkbox = self.page.locator('[class="rct-checkbox"]')
        self.__success_notification = self.page.locator('[id="result"]')

    def click_home_chb(self) -> None:
        self.__home_checkbox.click()

    def check_success_notification_shown(self) -> None:
        self.__success_notification.wait_for(state='visible')
        expect(self.__success_notification).to_contain_text(expected="You have selected")
