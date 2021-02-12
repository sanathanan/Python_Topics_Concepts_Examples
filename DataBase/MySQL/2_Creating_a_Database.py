# Creating a Database

import mysql.connector as connection

try:
    mydb=connection.connect(host="localhost",user="root",passwd="1234")
    
    # Creating a cursor to execute the query and display the output. It acts as a pointer
    cursor = mydb.cursor()
    
    # Giving our query
    query="CREATE DATABASE STUDENT;"
    
    # Excuting the query using cursor
    cursor.execute(query)
    print("Database Created")
    
    mydb.commit()
    
except Exception as e:
    print(str(e))

finally:
    # Closing the database
    mydb.close()

