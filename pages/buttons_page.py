from playwright.sync_api import Page


class Buttons:

    def __init__(self, page: Page):
        self.page = page
        self.doubleClickBtn = self.page.locator('[id="doubleClickBtn"]')
        self.rightClickBtn = self.page.locator('button[id="rightClickBtn"]')
        self.clickMeBtn = self.page.locator('//button[text()="Click Me"]')

        self.doubleClickBtnNotification = self.page.locator('[id="doubleClickMessage"]')
        self.rightClickBtnNotification = self.page.locator('p[id="rightClickMessage"]')
        self.clickMeBtnNotification = self.page.locator('p[id="dynamicClickMessage"]')

    def doubleClickBtn(self) -> None:
        self.doubleClickBtn.click(click_count=2)

    def checkDoubleClickNotificationShown(self) -> None:
        self.doubleClickBtnNotification.wait_for(state='visible')
        assert self.doubleClickBtnNotification.text_content() == 'You have done a double click'

    def rightClickBtn(self) -> None:
        self.rightClickBtn.click(button="right")

    def checkRightClickNotificationShown(self) -> None:
        self.rightClickBtnNotification.wait_for(state='visible')
        assert self.rightClickBtnNotification.text_content() == 'You have done a right click'

    def clickBtn(self) -> None:
        self.clickMeBtn.click()

    def checkClickNotificationShown(self) -> None:
        self.clickMeBtnNotification.wait_for(state='visible')
        assert self.clickMeBtnNotification.text_content() == 'You have done a dynamic click'
