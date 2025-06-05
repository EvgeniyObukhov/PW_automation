import pytest
from tests.ui.pages.text_box_page import TextBoxPage


@pytest.mark.ui
class TestTextBox:
    def test_text_box_form_submission(self, page):
        """Проверяем отправку формы Text Box"""
        text_box_page = TextBoxPage(page)

        # 1. Открываем страницу
        text_box_page.navigate()

        # 2. Заполняем форму
        test_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "address": "123 Main St, City"
        }
        text_box_page.fill_form(**test_data)

        # 3. Отправляем форму
        text_box_page.submit_form()

        # 4. Проверяем результат
        result = text_box_page.get_output()
        assert result["name"] == f"Name:{test_data['name']}"
        assert result["email"] == f"Email:{test_data['email']}"
        assert test_data["address"] in result["address"]  # Адрес может форматироваться