import mysql.connector
from faker import Faker
import random

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='class-password',
    database='testdatabase'

)
cursor = db_connection.cursor()
faker = Faker()

for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)
    cursor.execute(sql, values)