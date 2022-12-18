from django.test import TestCase
from autenticacao.models import User

class TestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_test_user(self):
        user = User.objects.create_user(username='teste2', email='teste2@gmail.com')
        user.set_password('senha2')
        user.save()
        return user

    def tearDown(self) -> None:
        print('\nTeste Encerrado!')
        return super().tearDown()