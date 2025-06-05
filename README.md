# QA Automation Project

## Stack:
- Python 3.10+
- Pytest
- Playwright (for UI)
- Allure reporting

## How to run:
```bash
pytest tests/ --alluredir=reports/allure
allure serve reports/allure


### 3. Конфигурация (`configs/`)
**`configs/base_config.py`**:
```python
class BaseConfig:
    BASE_URL = "https://api.example.com"
    API_TIMEOUT = 10
    UI_TIMEOUT = 15