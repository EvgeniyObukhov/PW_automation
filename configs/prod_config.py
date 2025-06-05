from .base_config import BaseConfig


class ProdConfig(BaseConfig):
    """Конфигурация для production-окружения"""

    # 1. API-настройки (переопределяем базовые)
    API_BASE_URL = "https://api.production.com"
    API_TIMEOUT = 15  # Увеличиваем таймаут для продовой среды

    # 2. Настройки Playwright
    HEADLESS = True  # Обязательно headless-режим в prod
    SLOW_MO = 0  # Без искусственных задержек

    # 3. Безопасность (значения берутся ТОЛЬКО из .env)
    TEST_USER = None  # Переопределяем, чтобы не было дефолтных значений
    TEST_PASSWORD = None

    # 4. Дополнительные prod-специфичные параметры
    SCREENSHOTS_ON_FAILURE = False  # Отключаем скриншоты в prod для скорости
    ALLURE_ATTACH_BODY = False  # Не прикрепляем тела запросов в отчет

    @classmethod
    def get_db_credentials(cls):
        """Пример метода для безопасного получения секретов"""
        from dotenv import load_dotenv
        import os

        load_dotenv()  # Явная загрузка .env
        return {
            'host': os.getenv('PROD_DB_HOST'),
            'user': os.getenv('PROD_DB_USER'),
            'password': os.getenv('PROD_DB_PASSWORD')
        }