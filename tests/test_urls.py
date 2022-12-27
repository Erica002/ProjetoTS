from django.urls import reverse
from django.contrib.messages import get_messages
from .test_base import TestBase
import logging

logger = logging.getLogger('django.request')
logger.setLevel(logging.ERROR)

class TestUrls(TestBase):
    #----- TESTE URLS APP AUTENTICACAO ----- #
    def test_exibe_pagina_cadastro(self):
        response = self.client.get(reverse('cadastro-usuario'))
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, "autenticacao/cadastro-usuario.html")

    def test_exibe_pagina_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, "autenticacao/login.html")

    #----- TESTE URLS APP MAIN ----- #
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
