import pytest

@pytest.fixture
def auth_token(api_client):
    response = api_client.login("test_user", "pass")
    return response.json()["token"]