# modules
import mysql.connector
from mysql.connector import errorcode


try:                           #!This path below is to avoid showing my DB credentials!
  cnx = mysql.connector.connect(read_default_file='C:/Users/MAYSA/.my.cnf') 
  print("connection successful!")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()