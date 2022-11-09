import string

from playwright.sync_api import Page


class Textbox:

    def __init__(self, page: Page):
        # double underscore for locators be private

        self.page = page
        self.__full_name_input = self.page.locator('[id="userName"]')
        self.__email_input = self.page.locator('[id="userEmail"]')
        self.__current_address_input = self.page.locator('[id="currentAddress"]')
        self.__submit_btn = self.page.locator('[id="submit"]')

        self.__full_name_notification = self.page.locator('[id="name"]')
        self.__email_notification = self.page.locator('[id="email"]')
        self.__current_address_notification = self.page.locator('p[id="currentAddress"]')

    def click_submit_btn(self) -> None:
        self.__submit_btn.click()

    def fill_full_name_input(self, name: string) -> None:
        self.__full_name_input.fill(name)

    def check_full_name_notification_shown(self) -> None:
        self.__full_name_notification.wait_for(state='visible')
        assert self.__full_name_notification.text_content() == 'Name:Dima'

    def fill_email_input(self, email: string) -> None:
        self.__email_input.fill(email)

    def check_email_notification_shown(self) -> None:
        self.__email_notification.wait_for(state='visible')
        assert self.__email_notification.text_content() == 'Email:hello@gmail.com'

    def fill_current_address_input(self, email: string) -> None:
        self.__current_address_input.fill(email)

    def check_current_address_notification_shown(self) -> None:
        self.__current_address_notification.wait_for(state='visible')
        assert self.__current_address_notification.inner_text() == "Current Address :Lviv"





