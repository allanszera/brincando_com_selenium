import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Edge()



try:
    # Abre a página inicial
    driver.get("https://books.toscrape.com/")  # Substitua pela URL inicial

    # Lista para armazenar os resultados
    resultados = []

    while True:
        # Aguarda até que os artigos estejam presentes na página
        artigos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
        )

        # Itera pelos artigos para extrair títulos e preços
        for artigo in artigos:
            titulo = artigo.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            preco = artigo.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()
            resultados.append(f"{titulo} - {preco}")

        # Tenta encontrar o botão "next"
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li.next a"))
            )
            # Clica no botão "next"
            next_button.click()
            time.sleep(2)  # Pequena pausa para o carregamento da página
        except:
            # Se o botão "next" não for encontrado, significa que chegamos à última página
            break

    # Imprime os resultados
    for resultado in resultados:
        print(resultado)

    # Cria um DataFrame com os resultados
    df = pd.DataFrame(resultados)

    # Exibe o DataFrame
    print(df)

finally:
    # Fecha o navegador
    driver.quit()
