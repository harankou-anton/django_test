from products.models import Product
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestIndex:
    def setup_method(self):
        self.client = APIClient()

    def test_my_function(self):
        response = self.client.get("/api/products/")
        assert response.status_code == 200
        assert len(response.json()) == 0

        response = self.client.post("/api/products/", data={
            "title": "title",
            "price": 250,
            "description": "description",
            "color": "BLUE",
        }, follow=True)
        assert response.status_code == 201
        assert Product.objects.exists()

    def test_delete_product(self):
        product = Product.objects.create(title='for_delete', price=500)
        response = self.client.get(f"/api/products/{product.id}/")
        assert response.status_code == 200
        assert response.json()['title'] == 'for_delete'

        response = self.client.delete(f"/api/products/{product.id}/")
        assert response.status_code == 204
        assert not Product.objects.exists()

