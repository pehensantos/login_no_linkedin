from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import time


navegador = Chrome()
navegador.get("https://www.linkedin.com/?original_referer=")
time.sleep(2)

caixa_de_login = navegador.find_element(By.CSS_SELECTOR, "#session_key")
caixa_de_login.click()
caixa_de_login.send_keys("**************")  #Inserir e-mail ou numero de telefone

caixa_de_senha = navegador.find_element(By.CSS_SELECTOR, "#session_password")
caixa_de_senha.click()
caixa_de_senha.send_keys("**********") #Inserir senha

botao_entrar = navegador.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button") #clicar no botao "Entrar"
botao_entrar.click()


time.sleep(50)
