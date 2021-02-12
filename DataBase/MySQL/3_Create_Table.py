# Create a Table Inside Databse

import mysql.connector as connection 

try:
    mydb=connection.connect(host="localhost", database="STUDENT", user="root", passwd="1234")
    
    cursor=mydb.cursor()
    
    # Creating a Table inside the database "STUDENT"
    query= """CREATE TABLE STUDENT_DETAILS(STUDENT_ID INT(10) AUTO_INCREMENT PRIMARY KEY,
                                        FIRST_NAME VARCHAR(60),
                                        LAST_NAME VARCHAR(60),
                                        REGISTRATION_DATE DATE,
                                        CLASS VARCHAR(30),
                                        SECTION VARCHAR(10)
                                        )"""
    cursor.execute(query)
    mydb.commit()

except Exception as e:
    print(str(e))
    
finally:
    mydb.close()


