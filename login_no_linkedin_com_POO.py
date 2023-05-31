from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class bot:
    def __init__(self):
        self.link = "https://www.linkedin.com/?original_referer="
        self.driver = Chrome()


    def abrir_site(self):
        self.driver.get(self.link)

    def fazer_login(self):
        caixa_de_login = self.driver.find_element(By.CSS_SELECTOR, "#session_key")
        caixa_de_login.click()
        caixa_de_login.send_keys("*******************") #Inserir email

        caixa_de_senha = self.driver.find_element(By.CSS_SELECTOR, "#session_password")
        caixa_de_senha.click()
        caixa_de_senha.send_keys("*******************") #Inserir senha

        botao_entar = self.driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button")
        botao_entar.click()



linkedin = bot()
linkedin.abrir_site()
time.sleep(2)
linkedin.fazer_login()
time.sleep(50)
