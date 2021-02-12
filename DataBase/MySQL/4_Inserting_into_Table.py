# Inserting into Table

import mysql.connector as connection 

try:
    mydb=connection.connect(host="localhost", database="STUDENT", user="root", passwd="1234") 
    cursor=mydb.cursor()
    query="INSERT INTO STUDENT_DETAILS VALUES('1111','SANATHANAN','THANGARAJ','1988-05-05','LKG','B')"
    cursor.execute(query)
    mydb.commit()

except Exception as e:
    print(str(e))
    
finally:
    mydb.close()