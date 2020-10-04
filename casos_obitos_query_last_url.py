import mysql.connector
import ssl
import urllib.request as req

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="pesquisa_covid"
)

mycursor = mydb.cursor(dictionary=True)

query = """
        SELECT url FROM url_casos_obitos
        WHERE id = '0118facb-8ea9-4ee1-94f0-b5ec16362a62'
        """

mycursor.execute(query)

myresult = mycursor.fetchall()

for x in myresult:
    url_casos_obitos = x['url']
    
mycursor.close()

mydb.close()

request_ssl = ssl._create_unverified_context()
request = req.urlopen(url_casos_obitos, context = request_ssl)
with  open('data/casos_obitos_data_query.csv', 'w') as f:
    f.write(request.read().decode())
