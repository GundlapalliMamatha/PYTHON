import mysql.connector

conn=mysql.connector.connect(host="localhost",database="kkkk",user="root",password="shivababa@123")
print(conn)  

cursor=conn.cursor()
print(cursor)    

create="create table Employee (eno int,ename varchar(40),age int,ecity varchar(40),ecountry varchar(50))"
cursor.execute(create)

print("table created")

cursor.close()

conn.close()