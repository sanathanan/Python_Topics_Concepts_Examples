# Updating Data into Table

import mysql.connector as connection 

# Example 1: Updating the record
mydb=connection.connect(host="localhost", database="STUDENT", user="root", passwd="1234")

try:
    cursor=mydb.cursor()
    query="UPDATE STUDENT_DETAILS SET FIRST_NAME='LAVANYA', LAST_NAME='BALASUBRAMANIAN' WHERE STUDENT_ID=1111"
    cursor.execute(query)
    mydb.commit()
    
except Exception as e:
    print(str(e))
    
finally:
    mydb.close()


# Example 2:
# Updating the record and seeing the updated record in the output

mydb=connection.connect(host="localhost", database="STUDENT", user="root", passwd="1234")

try:
    cursor=mydb.cursor()
    query="UPDATE STUDENT_DETAILS SET FIRST_NAME='LAVANYAAAAA', LAST_NAME='THANGARAJ' WHERE STUDENT_ID=1111"
    cursor.execute(query)
    mydb.commit()
    
    
    query="SELECT * FROM STUDENT_DETAILS WHERE STUDENT_ID=1111"
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)
    mydb.commit()
    
    
except Exception as e:
    print(str(e))
    
finally:
    mydb.close()