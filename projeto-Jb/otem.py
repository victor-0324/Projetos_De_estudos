from os import write
import re 
import csv
from pandas.core.indexes.base import Index
import requests  
import pandas as pd
from bs4 import BeautifulSoup  
from datetime import datetime

# 1. Pegar conteudo HTML a partir da URL
url = "https://www.resultadofacil.com.br/resultado-do-jogo-do-bicho/PB/de-ontem" 
html = requests.get(url)  

if html.status_code != 200: 
        print(">> Falha na requisição! <<")
else:
    # content passa o conteúdo da página
    html_content = html.content
    # Parsear o conteúdo HTML buscado, para poder ficar mais estruturado de acordo com as tags HTML
    soup = BeautifulSoup(html_content, 'html.parser')

#cabeçarios premio,bicho,grupo..
cabecario = soup.select('th')[0 : 5]
bichos = soup.find_all('tbody', id=True)
data = soup.find_all('p', class_='h4')
#texte = bichos.contents[0]
tabela = soup.find_all('div', class_="list-group-item")  



with open("jogodobicho.csv", "a", encoding='utf-8') as ficheiro:
    writer =  csv.writer(ficheiro, quoting=csv.QUOTE_MINIMAL)    
    #nomes = ['premio','milhar','grupo','bicho']                                                      #                                       writer = csv.writer(f, delimiter=';')
    #writer = csv.DictWriter(ficheiro, fieldnames=nomes)
    for intems in bichos:        
        csv_row = []
        for cell in intems.findAll(["td"]):           
            csv_row.append(cell.get_text()) 
        
        writer.writerow(csv_row)    
print(csv_row)

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Current time: {now}") 
        



