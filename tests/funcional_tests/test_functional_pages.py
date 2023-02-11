import os
import time
from time import sleep
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class FunctionalTest(TestCase, LiveServerTestCase):
   def test_exibe_login_page(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)
      sleep(2)
      browser.quit()

   def test_login_function_page(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      sleep(5)
        
      browser.quit()

   def test_exibe_cadastro_page(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 3)
      sleep(2)
      register = wait.until(EC.presence_of_element_located((By.ID, 'cadastro')))
      register.click()
      sleep(3)
      browser.quit()

   def test_cadastro_usuario_page(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/cadastro-usuario")
      wait = WebDriverWait(browser, 15)

      username = browser.find_element(By.NAME, "username")
      username.send_keys("Usuário23")
      sleep(1)
      email = browser.find_element(By.NAME, "email")
      email.send_keys("usuario23@gmail.com")
      sleep(1)
      password = browser.find_element(By.NAME,"password")
      password.send_keys("gf123456")
      sleep(1)
      request = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
      request.click()
      sleep(5)
        
      browser.quit()

   def test_create_wish(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      wish = wait.until(EC.presence_of_element_located((By.ID, 'list-wish')))
      wish.click()
      sleep(2)
      wish = wait.until(EC.presence_of_element_located((By.ID, 'add-wish')))
      wish.click()
      detalhes = browser.find_element(By.NAME, "detalhes")
      detalhes.send_keys("Carregador")
      sleep(1)
      valor_necessario = browser.find_element(By.NAME, "valor_necessario")
      valor_necessario.send_keys(150)
      sleep(1)
      valor_salvo = browser.find_element(By.NAME, "valor_salvo")
      valor_salvo.send_keys(0)
      sleep(1)
      data = browser.find_element(By.NAME, "data")
      data.send_keys("11/02/2023")
      sleep(4)
      request = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
      request.click()
      sleep(5)
        
      browser.quit()


   def test_create_categoria(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      categoria = wait.until(EC.presence_of_element_located((By.ID, 'list-categoria')))
      categoria.click()
      sleep(2)
      categoria = wait.until(EC.presence_of_element_located((By.ID, 'add-categoria')))
      categoria.click()
      nome = browser.find_element(By.NAME, "nome")
      nome.send_keys("Manutenção de equipamento")
      sleep(2)
      request = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
      request.click()
      sleep(5)
        
      browser.quit()


   def test_create_despesa(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      despesa = wait.until(EC.presence_of_element_located((By.ID, 'add-gasto')))
      despesa.click()
      detalhes = browser.find_element(By.NAME, "detalhes")
      detalhes.send_keys("Notebook")
      sleep(1)
      valor_despesa = browser.find_element(By.NAME, "valor_despesa")
      valor_despesa.send_keys(150)
      sleep(1)
      data = browser.find_element(By.NAME, "data")
      data.send_keys("11/02/2023")
      sleep(4)
      categoria = browser.find_element(By.NAME, "categoria")
      select = Select(categoria)
      select.select_by_visible_text("Teste")
      sleep(2)
      request = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
      request.click()
      sleep(5)
        
      browser.quit()



   def test_create_ganho(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      categoria = wait.until(EC.presence_of_element_located((By.ID, 'list-ganhos')))
      categoria.click()
      sleep(2)
      ganho = wait.until(EC.presence_of_element_located((By.ID, 'add-ganho')))
      ganho.click()
      detalhes = browser.find_element(By.NAME, "detalhes")
      detalhes.send_keys("Freelancer")
      sleep(1)
      valor_renda = browser.find_element(By.NAME, "valor_renda")
      valor_renda.send_keys(150)
      sleep(1)
      data = browser.find_element(By.NAME, "data")
      data.send_keys("11/02/2023")
      sleep(4)
      request = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
      request.click()
      sleep(5)
        
      browser.quit()


   def test_exibe_despesas_por_mes(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      categoria = wait.until(EC.presence_of_element_located((By.ID, 'grafico-mensal')))
      categoria.click()
      sleep(5)

      browser.quit()


   def test_exibe_despesas_por_ano(self):
      browser = webdriver.Chrome()
      browser.get("http://127.0.0.1:8000/autenticacao/login?next=/")
      wait = WebDriverWait(browser, 5)

      username = browser.find_element(By.NAME,"username")
      username.clear()
      username.send_keys("Érica")
      password = browser.find_element(By.NAME, "password")
      password.send_keys("gf123456")
      password.send_keys(Keys.RETURN)
      categoria = wait.until(EC.presence_of_element_located((By.ID, 'grafico-anual')))
      categoria.click()
      sleep(5)

      browser.quit()