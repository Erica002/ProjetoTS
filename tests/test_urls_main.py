from django.urls import reverse
from .test_base import TestBase
import logging

logger = logging.getLogger('django.request')
logger.setLevel(logging.ERROR)

class TestUrlsViews(TestBase):
    def test_index(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)
        
    def test_listagem_ganhos(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list-ganhos"))
        self.assertEqual(response.status_code, 200)

    def test_listagem_categoria(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list-categoria"))
        self.assertEqual(response.status_code, 200)

    def test_listagem_wishList(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list-wish"))
        self.assertEqual(response.status_code, 200)

    def test_mostra_grafico_renda_anual(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("grafico-renda-anual"))
        self.assertEqual(response.status_code, 200)

    def test_mostra_grafico_mensal_despesas(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("grafico-mensal"))
        self.assertEqual(response.status_code, 200)

    def test_mostra_grafico_anual_despesas(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("grafico-anual"))
        self.assertEqual(response.status_code, 200)