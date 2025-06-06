import pytest
from patchright.sync_api import Playwright, APIRequestContext
from configs.base_config import BaseConfig


"""@pytest.fixture(scope="function")
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
    browser.close()"""
@pytest.fixture(scope="function")
def page(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=False,  # Для дебага включаем видимый режим
        slow_mo=1000    # Замедление для наглядности
    )
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True  # Пропускаем SSL-ошибки
    )
    page = context.new_page()
    yield page
    context.close()
    browser.close()