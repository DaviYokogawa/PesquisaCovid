from bs4 import BeautifulSoup as bs # Importando BeautifulSoup
import requests # Importando Requests

url = 'https://www.saude.pr.gov.br/Pagina/Coronavirus-COVID-19' # Definindo URL
r = requests.get(url, headers={'User-Agent':'MyAgent'}) # Fazendo a request da URL
soup = bs(r.text, 'html.parser') # Extraindo todo o HTML com o BeautifulSoup

link_casos_obitos = [] # Ciando lista para receber os links de Casos e Óbitos.csv
for link in soup.find_all('a', text='Casos e Óbitos.csv'): # Loop for para encontrar os links dos arquivos csv
    link_casos_obitos.append(link.get('href'))

link_geral = [] # Ciando lista para receber os links de Geral.csv
for link in soup.find_all('a', text='Geral.csv'): # Loop for para encontrar os links dos arquivos csv
    link_geral.append(link.get('href'))

with open('data/casos_obitos.txt', 'w') as f: # Salvando os casos e obitos
    for i in link_casos_obitos:
        f.write('%s\n' % i)

with open('data/casos_geral.txt', 'w') as f: # Salvando os casos gerais
    for i in link_geral:
        f.write('%s\n' % i)