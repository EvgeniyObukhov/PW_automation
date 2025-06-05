from patchright.sync_api import Page
from configs.base_config import BaseConfig

class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BaseConfig.BASE_DEMOQA_URL  # Можно переопределить в .env

    def navigate(self):
        """Открывает страницу Text Box"""
        self.page.goto(f"{self.base_url}/text-box")

    def fill_form(self, name: str, email: str, address: str):
        """Заполняет форму Text Box"""
        # Локаторы
        self.page.fill("#userName", name)
        self.page.fill("#userEmail", email)
        self.page.fill("#currentAddress", address)
        self.page.fill("#permanentAddress", address)  # Для демо используем тот же адрес

    def submit_form(self):
        """Отправляет форму"""
        self.page.click("#submit")

    def get_output(self) -> dict:
        """Возвращает данные из результата"""
        return {
            "name": self.page.locator("#output #name").inner_text(),
            "email": self.page.locator("#output #email").inner_text(),
            "address": self.page.locator("#output #currentAddress").inner_text()
        }