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
        SELECT url FROM url_casos_geral
        WHERE id = '0093ebe8-191b-4f5e-bf12-fff681999b8d'
        """

mycursor.execute(query)

myresult = mycursor.fetchall()

for x in myresult:
    url_casos_geral = x['url']

mycursor.close()

mydb.close()

request_ssl = ssl._create_unverified_context()
request = req.urlopen(url_casos_geral, context = request_ssl)
with  open('data/casos_geral_data_query.csv', 'w') as f:
    f.write(request.read().decode())
