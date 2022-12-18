from django.urls import reverse
from django.contrib.messages import get_messages
from .test_base import TestBase

class TestViews(TestBase):
    def test_realiza_login(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'senha2'
        })
        self.assertEquals(response.status_code, 302)
        storage = get_messages(response.wsgi_request)
        self.assertIn(f'Bem-vindo(a), {user.username}',
                      list(map(lambda x: x.message, storage)))

    def test_nao_realiza_login_senha_invalida(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'senha'
        })
        
        self.assertEquals(response.status_code, 401)
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
        self.assertEquals(response.status_code, 302)

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
        self.assertEquals(response.status_code, 409)

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
        self.assertEquals(response.status_code, 409)

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
        self.assertEquals(response.status_code, 401)
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
        self.assertEquals(response.status_code, 401)

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
        self.assertEquals(response.status_code, 401)

        storage = get_messages(response.wsgi_request)
        self.assertIn("A senha deve ter no mínimo 6 caracteres",
                      list(map(lambda x: x.message, storage)))