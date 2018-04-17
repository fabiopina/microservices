import logging
import os
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# Logging configuration
logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')


# TODO: Sensitive information ºº
DATABASE = 'Users_MS'
TABLE = 'users'
USER = 'root'
PASSWORD = 'ribeiro'
HOST = os.environ['DATABASEADDRESS']
# TODO: Sensitive information ºº

# app is the object for flask managent
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE)
# db is now our orm manager
db = SQLAlchemy(app)

logging.debug("{ORM} Connecting into database ...")
while True:
    try:
        url = 'mysql+pymysql://%s:%s@%s' % (USER, PASSWORD, HOST)
        engine = create_engine(url)
        query = "CREATE DATABASE IF NOT EXISTS %s ;" % DATABASE
        engine.execute(query)
        db.create_all()
        db.session.commit()
    except Exception:
        logging.debug("{ORM} Database is down. Reconnecting in 5 seconds ....")
        time.sleep(5)
        continue
    break
