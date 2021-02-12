# Reading a file from Pandas

import mysql.connector as connection 
import pandas as pd

try:
    mydb=connection.connect(host="localhost",database="GLASSDATA", user="root", passwd="1234")
    #cursor = mydb.cursor()
    query="SELECT * FROM GLASS_DATA;"
    df=pd.read_sql(query,mydb)
    print("Reading a file using Pandas")
    for i in df:
        print(i)
        
    mydb.commit()

except Exception as e:
    print(str(e))

finally:
    mydb.close()

