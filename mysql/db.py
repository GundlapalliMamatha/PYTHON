import mysql.connector

conn=mysql.connector.connect(host="localhost",database="python",user="root",password="shivababa@123")
print("connection Tested")

conn.close


