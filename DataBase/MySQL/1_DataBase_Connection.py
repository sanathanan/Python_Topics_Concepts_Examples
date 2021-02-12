# Database Connection

# Importing mysql connector to make a connection between mysql database and Python code
import mysql.connector as connection

# Connecting through mysql database using host, username and password for the database
mydb=connection.connect(host="localhost", user="root", passwd="1234")

print("mydb is connected")

# Once database is opened, we need to close the database after use
mydb.close()



