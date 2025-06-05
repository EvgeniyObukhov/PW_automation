from .base_page import BasePage

class LoginPage(BasePage):
    @property
    def username_field(self):
        return "#username"

    def login(self, username, password):
        self.page.fill(self.username_field, username)
        self.page.fill("#password", password)
        self.click("#login-btn")