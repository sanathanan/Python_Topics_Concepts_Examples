# Looking data inside tables

# Inserting into Table - Example 1

import mysql.connector as connection 

try:
    mydb=connection.connect(host="localhost", database="STUDENT", user="root", passwd="1234") 
    cursor=mydb.cursor()
    query="SELECT * FROM STUDENT_DETAILS"
    cursor.execute(query)

    # fetchall() will display the output
    result=cursor.fetchall()
    print(result)
    
    mydb.commit()

except Exception as e:
    print(str(e))
    
finally:
    mydb.close()


# Inserting into Table - Example 2

import mysql.connector as connection 

try:
    mydb=connection.connect(host="localhost", database="STUDENT", user="root", passwd="1234") 
    cursor=mydb.cursor()
    query="SELECT * FROM STUDENT_DETAILS"
    cursor.execute(query)

    # fetchall() will display the output using forloop
    result=cursor.fetchall()
    for i in result:
        print(i)
        
    mydb.commit()

except Exception as e:
    print(str(e))
    
finally:
    mydb.close()
