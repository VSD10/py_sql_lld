import mysql.connector
from tabulate import tabulate


def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="db"
    )

    if connection: 
        return connection
    else:
        print("not connected")
        return None

def insert():
    con=get_connection()
    cursor=con.cursor()
    sql="insert into users(NAME,AGE,city,phone) values(%s,%s,%s,%s)"
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    city=input("Enter City")
    phone=int(input("Enter the number"))
    values=(name,age,city,phone)
    cursor.execute(sql,values)
    con.commit()
    print("Student added succesfully ID:",cursor.lastrowid)


def update():
    con = get_connection()
    cursor = con.cursor()

    id = int(input("Enter ID to change: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")
    phone = input("Enter Number: ")

    sql = "UPDATE users SET name=%s, age=%s, city=%s, phone=%s WHERE id=%s"
    vals = (name, age, city, phone, id)

    cursor.execute(sql, vals)
    con.commit()

    print("Updated successfully!")

    cursor.close()
    con.close()



def delete():
    con = get_connection()
    cursor = con.cursor()

    id = int(input("Enter ID to delete: "))

    sql = "DELETE FROM users WHERE id = %s"
    vals = (id,)

    cursor.execute(sql, vals)
    con.commit()

    print("Deleted successfully!")

    cursor.close()
    con.close()


def search():
    con = get_connection()
    if con is None:
        print("Connection failed!")
        return []

    cursor = con.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"ID   NAME")
    # for x in rows:
    #     print(f"{x[0]}  {x[1]}")

    print(tabulate(rows,headers=["ID","NAME","AGE","CITY","NUMBER"],tablefmt="grid"))

    cursor.close()
    con.close()
   





while True:
    print("\n\n\t\t\t\t\tWelcome to the student management system\n\n")
    print("1.New Student")
    print("2.Update Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")
    val=int(input("your option:: "))
    if val==1:
        insert()
    elif val==2:
        update()
    elif val==3:
        search()
    elif val==4:
        delete()
    elif val==5:
        quit()
    else:
        print("\n\n\nSelect the valid option!!!!\n\n")