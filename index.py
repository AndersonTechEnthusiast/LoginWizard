from selenium import webdriver # importa webdriver do selenium
from selenium.webdriver.chrome.options import Options # importa a Classe Options do selenium.webdriver.chrome.options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select # manipular tags <select> , <option>
import re
import pygetwindow as GW
import pyautogui
import time

# verifica o Email do Usuário

email_usuario = input("Digita seu Email: ")
regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
while not re.match(regex , email_usuario):
    print("Email Inválido")
    email_usuario = input("Digita seu Email: ") 

# verifica a Senha do Usuário

senha_usuario = input("Digita sua Senha: ")
while not senha_usuario: 
    print("sua senha não pode ser vazia !!!")
    senha_usuario = input("Digita sua Senha: ")

# configura o Service
caminho = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"
servico = Service(caminho)

# configura o Options
options = Options()

# --disable-blink-features=AutomationControlled:  Oculta que o Chrome está sendo controlado pelo Selenium, evitando restrições em sites.
options.add_argument('--disable-blink-features=AutomationControlled')

# --log-level=3 - impede mensagens de automação
options.add_argument('--log-level=3')

driver = webdriver.Chrome(service=servico , options=options)

pyautogui.click(x=1024 , y=130)

try:
    driver.get("https://google.com/")

    WebDriverWait(driver , 10).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME , "gb_Ta"))
    )

    fazer_login = WebDriverWait(driver , 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME , "gb_Ta"))
    )

    fazer_login.click()
    
    WebDriverWait(driver , 10).until(
        expected_conditions.visibility_of_element_located((By.ID , "identifierId"))
    )

    input_fazer_login_email = WebDriverWait(driver , 10).until(
        expected_conditions.element_to_be_clickable((By.ID , "identifierId"))
    )

    input_fazer_login_email.click()

    input_fazer_login_email.send_keys(email_usuario)

    input_fazer_login_email.send_keys(Keys.ENTER)

    while True: 
        try:
            email_incorreta = WebDriverWait(driver , 10).until(
                # condições esperadas
                # presenca de todos os elementos alocados
                # By - pelo , XPATH - caminho
                # [contains(text() , "text")] - puxa o texto que aparecer
                # "//*[contains(text() , "text")]" - todos os elementos que aparecem (//*) -> todos so resultados que satisfazem
                expected_conditions.presence_of_all_elements_located((By.XPATH , "//*[contains(text() , 'Não foi possível encontrar sua Conta do Google')]"))
            )

            time.sleep(2)

            driver.minimize_window()

            if email_incorreta:
                print("seu email ta incorreto !!!")
            
            email_corrigido = input("insira seu e-mail corrigido: \n Email: ")

            while not email_corrigido.strip():
                print("O Email Não Pode Ser Nulo !!!")
                email_corrigido = input("insira seu e-mail corrigido: \n Email: ")

            input_fazer_login_email = WebDriverWait(driver , 10).until(
                expected_conditions.element_to_be_clickable((By.ID , "identifierId"))
            )

            input_fazer_login_email.clear()

            input_fazer_login_email.click()

            input_fazer_login_email.send_keys(email_corrigido)

            input_fazer_login_email.send_keys(Keys.ENTER)
        except:
            driver.maximize_window()
            break

    WebDriverWait(driver , 10).until(
        expected_conditions.visibility_of_element_located((By.NAME , "Passwd"))
    )

    input_fazer_login_senha = WebDriverWait(driver , 10).until(
        expected_conditions.element_to_be_clickable((By.NAME , "Passwd"))
    )
    input_fazer_login_senha.click()

    input_fazer_login_senha.send_keys(senha_usuario)

    input_fazer_login_senha.send_keys(Keys.ENTER)

    time.sleep(2)
    
    # enquanto estiver True (verdadeiro) , mantenho o Loop
    while True:
        # tenta
        try: 
            # verifica se a mensagem: 
            # 'Senha incorreta. Tente novamente ou clique em \"Esqueceu a senha?\" para escolher outra.' - aparece
            senha_incorreta = WebDriverWait(driver , 5).until(
                expected_conditions.presence_of_all_elements_located((By.XPATH , "//*[contains(text() , 'Senha incorreta. Tente novamente ou clique em \"Esqueceu a senha?\" para escolher outra.')]"))
            )
            # espera 
            time.sleep(2)
            # minimiza a janela
            driver.minimize_window()
            # verifica se a mensagem existe
            if senha_incorreta:
                print("A senha que Você forneceu no inicio no sistema , está incorreta !!!")
            # cria um input novo para receber a senha corrigida 
            senha_corrigida = input("Insira sua Senha Corrigida agora por favor: \n Senha: ")
            # enquanto a senha for nula 
            while not senha_corrigida.strip():
                # mostre a mensagem 
                print("A senha não pode ser Nula por favor Insira sua Senha Corrigida")
                # dê o input enquanto a senha for nula
                senha_corrigida = input("Insira sua Senha Corrigida agora por favor: \n Senha: ")

            # procura o input da senha no driver (navegador)
            input_fazer_login_senha = WebDriverWait(driver , 10).until(
                expected_conditions.element_to_be_clickable((By.NAME , "Passwd"))
            )
            # limpa o input da senha do navegador
            input_fazer_login_senha.clear()
            # envia o que o usuário digitou 
            input_fazer_login_senha.send_keys(senha_corrigida)
            # pressione o Enter para acessar
            input_fazer_login_senha.send_keys(Keys.ENTER)
        except:
            # a mensagem não mais apareceu ? 
            # maxima a tela do driver
            driver.maximize_window()
            # quebra o Looping
            break
    
    input("Desativar")

except ValueError :
    print("Error")