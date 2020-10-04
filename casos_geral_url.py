import mysql.connector
import uuid

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="pesquisa_covid"
)

mycursor = mydb.cursor()
uid = str(uuid.uuid4())

with open("data/casos_geral.txt") as file:
    for line in file:
        uid = str(uuid.uuid4()) 
        sql = "INSERT INTO url_casos_geral (id, url) VALUES (%s, %s)"
        val = (uid, line)
        mycursor.execute(sql, val)

mydb.commit()

mydb.close()
