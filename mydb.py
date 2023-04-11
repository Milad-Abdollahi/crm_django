import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='toor'
)

# preparing cursor object
cursorObject = dataBase.cursor()

# creating a database
cursorObject.execute('CREATE DATABASE elderco')

print('finished creating database!')
