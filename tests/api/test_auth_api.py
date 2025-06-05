import pytest

@pytest.mark.api
class TestAuthAPI:
    def test_login_success(self, api_client):
        response = api_client.login("valid_user", "valid_pass")
        assert response.status_code == 200
        assert "token" in response.json()