# connecting to mysql database
import mysql.connector

print("connecting to db ...")
cnx = mysql.connector.connect(user='samane', password='', host='127.0.0.1', database='learn')
print('connected to db successfully.')

name = 'shahab'
age = 30
sex = 'm'

cursor = cnx.cursor()
cursor.execute('INSERT INTO people VALUES ("%s", %i, "%s")' % (name, age, sex))

cnx.commit()
cnx.close()
