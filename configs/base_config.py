import os
from dotenv import load_dotenv
from pathlib import Path

# Загружаем переменные из .env (если файл существует)
load_dotenv()


class BaseConfig:
    """Базовый конфиг, используемый во всех окружениях"""

    # 1. Общие настройки
    PROJECT_ROOT = Path(__file__).parent.parent
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # DEBUG, INFO, WARNING
    BASE_DEMOQA_URL = "https://demoqa.com"

    # 2. API-настройки
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 10))  # в секундах
    API_MAX_RETRIES = 3

    # 3. Настройки Playwright (UI)
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chromium")  # chromium, firefox, webkit
    SLOW_MO = int(os.getenv("SLOW_MO", 0))  # замедление для отладки (мс)
    VIEWPORT = {"width": 1920, "height": 1080}

    # 4. Настройки отчетов
    ALLURE_DIR = os.getenv("ALLURE_DIR", str(PROJECT_ROOT / "reports" / "allure"))
    SCREENSHOTS_DIR = PROJECT_ROOT / "reports" / "screenshots"

    # 5. Авторизационные данные (для примера, лучше хранить в .env)
    TEST_USER = os.getenv("TEST_USER", "test_user@example.com")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "default_password")

    @classmethod
    def setup_dirs(cls):
        """Создает необходимые директории"""
        os.makedirs(cls.ALLURE_DIR, exist_ok=True)
        os.makedirs(cls.SCREENSHOTS_DIR, exist_ok=True)