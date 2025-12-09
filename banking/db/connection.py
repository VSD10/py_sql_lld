import mysql.connector


def connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="banker"
        )
    if con:
        print("connected")
        return con
       
    else:
        print("not connected")
        return 
           
        