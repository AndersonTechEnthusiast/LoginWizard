from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from guara.transaction import AbstractTransaction, Application
from guara import setup, it
import re
import time


# Transaction para abrir o Google
class AbrirGoogle(AbstractTransaction):
    def do(self, **kwargs):
        url = kwargs.get("url", "https://google.com/")
        self._driver.get(url)
        WebDriverWait(self._driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "gb_Ta"))
        )
        return True


# Transaction para realizar login
class RealizarLogin(AbstractTransaction):
    def do(self, **kwargs):
        email = kwargs["email"]
        senha = kwargs["senha"]

        # Inserir email
        input_email = WebDriverWait(self._driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "identifierId"))
        )
        input_email.click()
        input_email.send_keys(email)
        input_email.send_keys(Keys.ENTER)

        # Validar email incorreto
        while True:
            try:
                WebDriverWait(self._driver, 5).until(
                    expected_conditions.presence_of_all_elements_located(
                        (
                            By.XPATH,
                            "//*[contains(text(), 'Não foi possível encontrar sua Conta do Google')]",
                        )
                    )
                )
                print("Email incorreto!")
                email_corrigido = input("Digite o email corrigido: ").strip()
                input_email = WebDriverWait(self._driver, 10).until(
                    expected_conditions.element_to_be_clickable((By.ID, "identifierId"))
                )
                input_email.clear()
                input_email.send_keys(email_corrigido)
                input_email.send_keys(Keys.ENTER)
            except:
                break

        # Inserir senha
        input_senha = WebDriverWait(self._driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, "Passwd"))
        )
        input_senha.click()
        input_senha.send_keys(senha)
        input_senha.send_keys(Keys.ENTER)

        # Validar senha incorreta
        while True:
            try:
                WebDriverWait(self._driver, 5).until(
                    expected_conditions.presence_of_all_elements_located(
                        (By.XPATH, "//*[contains(text(), 'Senha incorreta.')]")
                    )
                )
                print("Senha incorreta!")
                senha_corrigida = input("Digite a senha corrigida: ").strip()
                input_senha = WebDriverWait(self._driver, 10).until(
                    expected_conditions.element_to_be_clickable((By.NAME, "Passwd"))
                )
                input_senha.clear()
                input_senha.send_keys(senha_corrigida)
                input_senha.send_keys(Keys.ENTER)
            except:
                break

        return "Login realizado com sucesso!"


# Transaction para finalizar a execução
class FecharDriver(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.quit()


# Teste utilizando o padrão Page Transactions
def test_google_login():
    # Configurar o WebDriver
    caminho = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"
    servico = Service(caminho)
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=servico, options=options)

    # Configurar a aplicação
    app = Application(driver)

    # Solicitar credenciais do usuário
    email_usuario = input("Digite seu email: ").strip()
    senha_usuario = input("Digite sua senha: ").strip()

    # Executar transações
    app.at(AbrirGoogle, url="https://google.com/")
    resultado_login = app.at(RealizarLogin, email=email_usuario, senha=senha_usuario)
    print(resultado_login)
    app.at(FecharDriver)


# Rodar o teste
if __name__ == "__main__":
    test_google_login()
