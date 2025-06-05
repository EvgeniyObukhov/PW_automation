import pytest
from playwright.sync_api import Page
from configs.dev_config import DevConfig
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def config():
    return DevConfig()

@pytest.fixture
def api_client(config):
    # Здесь можно инициализировать клиент для API
    yield APIClient(config.BASE_URL)