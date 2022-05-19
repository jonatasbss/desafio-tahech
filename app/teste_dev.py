from selenium import webdriver
from selenium.webdriver.common.by import By


class Licitacoes:
    def __init__(self):
        self.quantidade = ""
        self.valor = ""

    def procura(self):
        url = "https://www.portaltransparencia.gov.br/licitacoes?ano=2022"

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Sem abertura do navegador
        options.add_argument("start-maximized")  # Início maximizado
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-blink-features=AutomationControlled")  # Previne detecção do Selenium
        options.add_argument("--no-sandbox")  # Tratativa do erro DevToolsActivePort file doesn't exist
        options.add_argument("--disable-dev-shm-usage")  # Tratativa do erro DevToolsActivePort file doesn't exist
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        driver.maximize_window()

        try:
            dados = driver.find_elements(By.XPATH, '//strong//span')
        except Exception as e:
            dados = ""

        for dado in dados:
            dado = dado.text

            if dado.__contains__("R$"):
                self.valor = dado

            else:
                self.quantidade = dado

        return self.quantidade, self.valor


# if __name__ == "__main__":
#     carf = Licitacoes()
#     quantidade, valor = carf.procura()
#
#     print("QUANTIDADE DE LICITAÇÕES COM CONTRATAÇÃO: ", quantidade)
#     print("VALOR TOTAL DAS CONTRATAÇÕES", valor)
