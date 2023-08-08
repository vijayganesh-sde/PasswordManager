import mysql.connector
def dbconfig():
  conn=mysql.connector.connect(user="root", host="Localhost", database="passManager")
  return conn

