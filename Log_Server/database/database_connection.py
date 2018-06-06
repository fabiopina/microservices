import mysql.connector as conn
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def connect():
    host = config.get('MySQL', 'host')
    user = config.get('MySQL', 'user')
    password = config.get('MySQL', 'password')
    database = config.get('MySQL', 'db_name')
    charset = config.get('MySQL', 'charset')

    db = conn.connect(host=host, user=user, password=password, charset=charset)
    cursor = db.cursor()
    # Create database
    cursor.execute("""CREATE DATABASE IF NOT EXISTS data""")
    db.commit()
    # Connect to database created before
    db = conn.connect(host=host, database=database, user=user, password=password, charset=charset)
    return db

