# Creating a Database
#Creating a Table
# Reading the file 
    # Inserting the data from the file into database
    

import mysql.connector as connection 
import csv


# Creating a Database
try:
    mydb=connection.connect(host="localhost",user="root",passwd="1234")
    cursor=mydb.cursor()
    query="CREATE DATABASE IF NOT EXISTS GLASSDATA"
    cursor.execute(query)
    print("Database Created")
    mydb.close()
    
    
    # Creating a Table
    mydb=connection.connect(host="localhost",database="GLASSDATA", user="root",passwd="1234")
    cursor=mydb.cursor()
    query="""CREATE TABLE IF NOT EXISTS GLASS_DATA (INDEX_NUMBER INT(10),
                                                   RI FLOAT(10,5),
                                                   NA FLOAT(10,5),
                                                   MG FLOAT(10,5),
                                                   AL FLOAT(10,5),
                                                   SI FLOAT(10,5),
                                                   K FLOAT(10,5),
                                                   CA FLOAT(10,5),
                                                   BA FLOAT(10,5),
                                                   FE FLOAT(10,5),
                                                   CLASS INT(5))"""
    cursor.execute(query)
    print("Table Created")

    
    
    # Reading from the file and inseting data from file to table
    
    with open("glass.data", "r") as f:
        next(f)
        glass_data=csv.reader(f, delimiter="\n")
        for line in enumerate(glass_data):
            for list_ in (line[1]):
                cursor.execute("INSERT INTO GLASS_DATA VALUES ({values})".format(values=(list_)))
        print("Data Inserted")
        mydb.commit()
    
except Exception as e:
    print(str(e))
    
finally:
    mydb.close()
            

