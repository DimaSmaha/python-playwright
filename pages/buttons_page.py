from playwright.sync_api import Page


class Buttons:

    def __init__(self, page: Page):
        # double underscore for locators be private

        self.page = page
        self.__double_click_btn = self.page.locator('button[id="doubleClickBtn"]')
        self.__right_click_btn = self.page.locator('button[id="rightClickBtn"]')
        self.__click_me_btn = self.page.locator('//button[text()="Click Me"]')

        self.__double_click_btn_notification = self.page.locator('[id="doubleClickMessage"]')
        self.__right_click_btn_notification = self.page.locator('p[id="rightClickMessage"]')
        self.__click_me_btn_notification = self.page.locator('p[id="dynamicClickMessage"]')

    def click_double_click_btn(self) -> None:
        self.__double_click_btn.click(click_count=2)

    def check_double_click_notification_shown(self) -> None:
        self.__double_click_btn_notification.wait_for(state='visible')
        assert self.__double_click_btn_notification.text_content() == 'You have done a double click'

    def click_right_click_btn(self) -> None:
        self.__right_click_btn.click(button="right")

    def check_right_click_notification_shown(self) -> None:
        self.__right_click_btn_notification.wait_for(state='visible')
        assert self.__right_click_btn_notification.text_content() == 'You have done a right click'

    def clickBtn(self) -> None:
        self.__click_me_btn.click()

    def check_dynamic_click_notification_shown(self) -> None:
        self.__click_me_btn_notification.wait_for(state='visible')
        assert self.__click_me_btn_notification.text_content() == 'You have done a dynamic click'
