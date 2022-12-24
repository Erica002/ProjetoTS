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

class TestViews(TestBase):
    def test_exibe_pagina_cadastro(self):
        response = self.client.get(reverse('cadastro-usuario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "autenticacao/cadastro-usuario.html")

    def test_exibe_pagina_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "autenticacao/login.html")

    def test_realiza_login(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'senha2'
        })
        self.assertEqual(response.status_code, 302)
        storage = get_messages(response.wsgi_request)
        self.assertIn(f'Bem-vindo(a), {user.username}',
                      list(map(lambda x: x.message, storage)))

    def test_nao_realiza_login_senha_invalida(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'senha'
        })
        
        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn("Nome de usuário ou senha inválida, tente novamente",
                      list(map(lambda x: x.message, storage)))

    def test_cadasto_usuario(self):
        data = {
            "username": "teste3",
            "email": "teste3@gmail.com",   
            "password":"senha1"
        }
        response = self.client.post(reverse("cadastro-usuario"), data)
        self.assertEqual(response.status_code, 302)

    def test_nao_deve_cadastrar_username_ja_utilizado(self):
        data = {
            "username": "teste3",
            "email": "teste4@gmail.com",   
            "password":"senha4"
        }
        # Realza o cadastro de usuário.
        self.client.post(reverse("cadastro-usuario"), data)
        # Faz request para cadastrar usuário novamente, que deve falhar uma vez que o nome de usuário está em uso. 
        response = self.client.post(reverse("cadastro-usuario"), data) 
        self.assertEqual(response.status_code, 409)

        storage = get_messages(response.wsgi_request)
        self.assertIn('Esse nome de usuário já está em uso. Escolha um diferente',
                      list(map(lambda x: x.message, storage)))

    def test_nao_pode_cadastrar_email_ja_utilizado(self):
        data_teste = {
            "username": "teste4",
            "email": "teste4@gmail.com",
            "password": "senha1"
        }

        data_teste2 = {
            "username": "teste5",
            "email": "teste4@gmail.com",
            "password": "senha5"
        }
        # Cadastra o primeiro usuário
        self.client.post(reverse("cadastro-usuario"), data_teste) 
        # Retorna mensagem de erro no segundo, devido ao email já estar sendo utilizado por outro usuário
        response = self.client.post(reverse("cadastro-usuario"), data_teste2) 
        self.assertEqual(response.status_code, 409)

        storage = get_messages(response.wsgi_request)
        self.assertIn('Esse email já está em uso. Escolha um diferente',
                      list(map(lambda x: x.message, storage)))

    def test_nao_pode_cadastrar_email_com_formato_invalido(self):
        data = {
            "username": "teste6",
            "email": "test&6#!gmail.com",
            "password": "senha6"
        }

        response = self.client.post(reverse("cadastro-usuario"), data)
        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn("Insira um formato de email válido",
                      list(map(lambda x: x.message, storage)))

    def test_nao_pode_cadastrar_usuario_nao_informado(self):
        data = {
            "username": "",
            "email": "teste7@gmail.com",   
            "password":"senha7"
        }
        response = self.client.post(reverse("cadastro-usuario"), data)
        self.assertEqual(response.status_code, 401)

        storage = get_messages(response.wsgi_request)
        self.assertIn("É preciso informar um nome de usuário",
                      list(map(lambda x: x.message, storage)))

    def test_nao_deve_cadastrar_senha_com_menos_de_seis_caracteres(self):
        data = {
            "username": "teste8",
            "email": "teste8@gmail.com",   
            "password":"senha"
        }
        response = self.client.post(reverse("cadastro-usuario"), data)
        self.assertEqual(response.status_code, 401)

        storage = get_messages(response.wsgi_request)
        self.assertIn("A senha deve ter no mínimo 6 caracteres",
                      list(map(lambda x: x.message, storage)))

    def test_faz_logout_usuario(self):
        response = self.client.get(reverse("logout"), follow=True)
        self.assertEqual(response.status_code, 200)

    #----- TESTE APP MAIN ----- #
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

        
    def setUp(self):
        user = User.objects.create(username="TantoFaz", email="test")
        user.set_password("senha12")
        user.save()
        self.clientC = Client()
        self.client.login(username="TantoFaz", password="senha12")
        self.categoriaD = Categoria.objects.create(nome="CategoriaTeste",user=user)
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
