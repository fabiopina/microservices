import mysql.connector as conn

db = conn.connect(host='localhost', database='data', user='root', password='ribeiro')

cursor=db.cursor()
#create database
cursor.execute("""CREATE DATABASE IF NOT EXISTS Testdb""")
db.commit()
