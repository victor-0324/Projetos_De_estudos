from os import write
import re 
import csv
from matplotlib.pyplot import table
from pandas.core.indexes.base import Index
import requests  
import pandas as pd
from bs4 import BeautifulSoup  
from datetime import datetime
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Current time: {now}") 


# 1. Pegar conteudo HTML a partir da URL
url = "https://www.resultadofacil.com.br/resultado-do-jogo-do-bicho/PB/" 
html = requests.get(url)  

if html.status_code != 200: 
        print(">> Falha na requisição! <<")
else:
    # content passa o conteúdo da página
    html_content = html.content
    # Parsear o conteúdo HTML buscado, para poder ficar mais estruturado de acordo com as tags HTML
    soup = BeautifulSoup(html_content, 'html.parser')

#cabeçarios premio,bicho,grupo..
cabecario = soup.select('b')[0 : 5]
bichos = soup.find_all('tbody', id=True)
data = soup.find_all('h3', class_='g')
tabela = soup.find_all('div', class_="col-sm-12 col-md-6 col-lg-4")  
bicho_20hrs = soup.find_all('tbody', id_="tbody-106053058571") 

with open("jogo_do_bicho2.csv", "a", encoding='utf-8') as ficheiro:
    writer =  csv.writer(ficheiro, quoting=csv.QUOTE_MINIMAL)                                                         #                                       writer = csv.writer(f, delimiter=';')
    for intems in tabela:              
        csv_row = []
        for cell in intems.findAll([{"td","p"}]):           
            csv_row.append(cell.get_text())           
                
        writer.writerow(csv_row)    
print(csv_row) 

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Current time: {now}")
        



