from django.contrib.auth.models import User
from django.test.client import Client
import pytest


@pytest.mark.django_db
class TestIndex:
    def setup_method(self):
        self.client = Client()

    def test_my_function(self):
        response = self.client.get("/register/")
        assert response.status_code == 200

        response = self.client.post("/register/", data={
            "email": "pytest@test.com",
            "first_name": "pytest@test.com",
            "last_name": "pytest@test.com",
            "user_name": "pytest@test.com",
            "password": "pytest@test.com",
            "age": 78
        }, follow=True)
        assert response.status_code == 200
        assert User.objects.exists()

        response = self.client.post("/login_view/", data={
            "email": "pytest@test.com",
            "password": "pytest@test.com",
        }, follow=True)
        assert response.status_code == 200