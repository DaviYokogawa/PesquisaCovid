import requests
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

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

casos_geral = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div/div[5]/div/p/strong/span/a')
casos_geral_exec = driver.execute_script("arguments[0].click();", casos_geral)
casos_geral_exec

req_geral = requests.get(driver.current_url)
url_geral_content = req_geral.content

csv_geral = open('casos_geral.csv', 'wb')
csv_geral.write(url_geral_content)
csv_geral.close()

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