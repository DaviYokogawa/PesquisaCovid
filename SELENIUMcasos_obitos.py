'''
Por motivos de alteração no formato do projeto não será mais utilizado
esse método de Web Scraping, por dois motivos:

1- Queremos ter em nosso banco de dados o histórico cronológico dos dados
e existem formas mais faceis de fazer isso

2- Ele funciona, porém é muito custoso computacionalmente coletar o arq.csv
então para datasets um pouco mais pesados como o Geral.csv já se torna mais 
difícil.
'''

import requests
from selenium import webdriver

# https://www.saude.pr.gov.br/Pagina/Coronavirus-COVID-19

PATH = "/Users/daviyokogawa/chromedriver"

url = 'https://www.saude.pr.gov.br/Pagina/Coronavirus-COVID-19'
driver = webdriver.Chrome(PATH)
options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')

driver.get(url)

boletim = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]')
driver.execute_script("arguments[0].click();", boletim)

driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
driver.implicitly_wait(10)

mes = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/div[1]/div[1]')
driver.execute_script("arguments[0].click();", mes)

driver.implicitly_wait(10)

casos_obitos = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/p/strong/span/a')
casos_obitos_exec = driver.execute_script("arguments[0].click();", casos_obitos)
casos_obitos_exec

req_casos_obitos = requests.get(driver.current_url)
url_casos_obitos_content = req_casos_obitos.content
print(url_casos_obitos_content)
csv_casos_obitos = open('casos_obitos.csv', 'wb')
csv_casos_obitos.write(url_casos_obitos_content)
csv_casos_obitos.close()

driver.quit()

'''
# XPATHS
###############################
boletimXpath =        //*[@id="content"]/div/div[1]/div[3]/div[1]
mesXpath     =        //*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/div[1]/div[1]
casos_obitosXpath =   //*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[2]/div/p/strong/span/a
geralXpath =          //*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[5]/div/p/strong/span/a
###############################
'''