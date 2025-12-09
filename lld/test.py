import mysql.connector

def get_connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="vsd"
    )
    cursor=con.cursor()
    cursor.execute("select * from word")
    print("row foubnd")
    row=cursor.fetchall()
    print(row)
get_connection()