__author__ = 'Dzmitry'
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * from group_list")
    for a in cursor.fetchall():
        print(a)
finally:
    connection.close()