import datetime
from django.urls import reverse
from django.contrib.messages import get_messages
from .test_base import TestBase
import logging
from main.models import Despesa, Wishlist, Renda, Categoria
from autenticacao.models import User
from django.test import Client

logger = logging.getLogger('django.request')
logger.setLevel(logging.ERROR)

class TestMainViews(TestBase):
    def setUp(self):
        user = User.objects.create(username="TantoFaz", email="test")
        user.set_password("senha12")
        user.save()
        self.clientC = Client()
        self.client.login(username="TantoFaz", password="senha12")
        self.categoriaD = Categoria.objects.create(nome="CategoriaTeste",user=user)
        self.categoriaT = Categoria.objects.create(nome="TesteCategoria",user=user)
        self.despesa = Despesa.objects.create(
            id=1,
            detalhes="Qualquer",
            valor_despesa=25,
            data=datetime.date(2022, 12, 23),
            categoria=self.categoriaD,
            user=user
            
            )

        self.receita = Renda.objects.create(
            id=1,
            detalhes="Extra",
            valor_renda=40,
            data=datetime.date(2022, 12, 23),
            user=user
            )

        self.wish = Wishlist.objects.create(
            id=1,
            detalhes="Jogo",
            valor_necessario=150,
            valor_salvo=50,
            user=user
            )
    
    def test_criar_despesa(self):
        response = self.client.post(
            reverse("add-gasto"),
            {
                "detalhes": "Teste",
                "valor_despesa": 50,
                "data": datetime.date(2022, 12, 23),
                "categoria": self.categoriaD,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_despesa(self):
        response = self.client.delete(
            reverse("delete-gasto", kwargs={"id": 1}), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_criar_receita(self):
        self.create_test_user()
        self.login()
        response_200 = self.client.post(reverse('add-ganho'), data={
            "detalhes": "Natal",
            "valor_renda": 100,
            "data": datetime.date(2022, 12, 23),

        }, follow=True)
        self.assertEqual(response_200.status_code, 200)

    def test_receita_update(self):
        response = self.client.post(
            reverse("update-ganhos", kwargs={"id": 1}),
            {
                "detalhes":" Natal",
                "valor_renda": 150,
                "data": datetime.date(2022, 12, 23),
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_receita(self):
        response = self.client.delete(
            reverse("delete-ganhos", kwargs={"id": 1}), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_criar_categoria(self):
        self.create_test_user()
        self.login()
        response_200 = self.client.post(reverse('add-categoria'), data={
            "nome": "Meu sobrinho"
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)

    def test_categoria_update(self):
        response = self.client.post(
            reverse("update-categoria", kwargs={"id": 1}),
            {
                "nome": "Meu sobrinho"
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_categoria(self):
        response = self.client.delete(
            reverse("delete-categoria", kwargs={"id": 1}), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_criar_wish(self):
        self.create_test_user()
        self.login()
        response_200 = self.client.post(reverse('add-wish'), data={
            "detalhes": "Cadeira nova",
            "valor_necessario": 300,
            "valor_salvo": 100,
            "data": datetime.date(2022, 12, 23),
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)

    def test_wish_update(self):
        response = self.client.post(
            reverse("update-wish", kwargs={"id": 1}),
            {
                "detalhes": "Cadeira nova",
                "valor_necessario": 300,
                "valor_salvo": 100,
                "data": datetime.date(2022, 12, 23),
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_wish(self):
        response = self.client.delete(
            reverse("delete-wish", kwargs={"id": 1}), follow=True
        )
        self.assertEqual(response.status_code, 200)
