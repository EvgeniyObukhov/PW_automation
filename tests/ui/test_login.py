import pytest
from playwright.sync_api import Page
from tests.ui.pages.login_page import LoginPage

@pytest.mark.ui
class TestLogin:
    def test_successful_login(self, page: Page):
        login_page = LoginPage(page)
        login_page.page.goto("/login")
        login_page.login("valid_user", "valid_pass")
        assert page.url.contains("/dashboard")