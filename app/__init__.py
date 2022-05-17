from flask import Flask
from .config import Config
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'capstone'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

from app import views