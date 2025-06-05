from patchright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 15000

    def click(self, selector):
        self.page.click(selector, timeout=self.timeout)