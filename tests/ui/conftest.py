import pytest
from patchright.sync_api import Playwright, APIRequestContext

from configs.base_config import BaseConfig


@pytest.fixture(scope="function")
def page(playwright: Playwright):
    # Запускаем браузер
    browser = playwright.chromium.launch(
        headless=BaseConfig.HEADLESS,
        slow_mo=BaseConfig.SLOW_MO
    )
    context = browser.new_context(viewport=BaseConfig.VIEWPORT)
    page = context.new_page()

    yield page

    # Закрываем после теста
    context.close()
    browser.close()