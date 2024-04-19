import mysql.connector
from faker import faker
import random

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='class-password',
    database='testdatabase'
)

cursor = db_connection.cursor()