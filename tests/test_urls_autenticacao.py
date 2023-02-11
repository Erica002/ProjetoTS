from django.urls import reverse
from .test_base import TestBase
import logging

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
