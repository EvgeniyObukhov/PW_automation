import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        return requests.post(
            f"{self.base_url}/auth/login",
            json={"username": username, "password": password}
        )