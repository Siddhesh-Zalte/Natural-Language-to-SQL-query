import sqlite3 
#cpnnectr = sqlite3.connect('example.db')
connectionn=sqlite3.connect("Student.db")

#create a cursor object to insert recoed cretae table, retrieve

cursor=connectionn.cursor()

#table inf0
table_info="""
CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)


#insert some records
cursor.execute("INSERT INTO STUDENT VALUES('John', '10', 'A', 85);")
cursor.execute("INSERT INTO STUDENT VALUES('Jane', '10', 'B', 90);")  
cursor.execute("INSERT INTO STUDENT VALUES('Doe', '10', 'C', 75);")
cursor.execute("INSERT INTO STUDENT VALUES('Alice', '10', 'A', 65);")

#Display on admin side
print("The records are:")
data=cursor.execute("SELECT * FROM STUDENT;")
for row in data:
    print(row)

#Close the connection
connectionn.commit()
connectionn.close()
