import mysql.connector
from tabulate import tabulate

# def create_db():
#     try:
#         con=mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="#Harinisri2012"
#         )
#         cursor=con.cursor()
#         cursor.execute("create database if not exists gymdb ")
#         print("database created successfully")

#     except Exception as e:
#         print("error while connection ",e)
#     finally:
#         try:
#             cursor.close()
#             con.close()
#         except:
#             pass

# def create_table():
#     try:
#         con=mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="#Harinisri2012",
#             database="gymdb"
#         )
#         cursor=con.cursor()
#         sql=""" create table if not exists members(
#             ID int auto_increment primary key,
#             name varchar(50),
#             age int,
#             phone varchar(15),
#             membership varchar(50),
#             start_date date
        
#         )
#             """
#         cursor.execute(sql)
#         print("table created successfully")
#     except Exception as e:
#         print("error while connections ",e)
#     finally:
#         try:
#             con.close()
#             cursor.close()
#         except:
#             pass

def get_connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="gymdb"
    )

    if con:
        return con
    else:
        print("database not connected!!!!!!")
        return None


def safeinput(value,cast):
    while True:
        try:
            val=cast(input(value))
            return val
        except Exception as e:
            print(e)
            
def newmem():
    con=get_connection()
    if con is None :
        return
    try:
        cursor=con.cursor()
        name=safeinput("Enter Name : ",str)
        age=safeinput("enter age : ",int)
        phone=safeinput("enter number : ",str)
        member=safeinput("enter membership type :",str)
        date=safeinput("Enter Start Date (YYYY-MM-DD): ",str)
        sql="insert into members(name,age,phone,membership,start_date) values(%s,%s,%s,%s,%s)"
        data=(name,age,phone,member,date)
        cursor.execute(sql,data)
        con.commit()
        print("Member added successfully")
    except Exception as e:
        print("had some issue ",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def printer(val):
    print(tabulate(val,headers=["ID","NAME","AGE","PHONE NUMBER","MEMBERSHIP","JOINED DATE"],tablefmt="grid"))



    

def update():
    con=get_connection()
    if not con:
        return 
    try:
        cursor=con.cursor()
        id=safeinput("enter id number to update:: ",int)
        name=safeinput("Enter Name : ",str)
        age=safeinput("enter age : ",int)
        phone=safeinput("enter number : ",str)
        member=safeinput("enter membership type :",str)
        date=safeinput("Enter Start Date (YYYY-MM-DD): ",str)
        sql="update members set name=%s, age=%s, phone=%s ,membership=%s ,start_date=%s where ID=%s"
        val=(name,age,phone,member,date,id)
        cursor.execute(sql,val)
        con.commit()
        print("Updated successfully")
    except Exception as e:
        print("error found ",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def delete():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        id=safeinput("enter a id to delete : ",int)
        sql="delete from members where ID=%s"
        cursor.execute(sql,(id,))
        con.commit()

        print("deleted successfully")
    except Exception as e:
        print("some trouble in creation",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def view():
    con=get_connection()
    if con is None:
        return
    try:
        cursor=con.cursor()
        sql="select * from members"
        cursor.execute(sql)
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error found ",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass


def searchbyphone():
    con=get_connection()
    if con is None:
        return
    try:
        cursor=con.cursor()
        phone=safeinput("enter a phone number: ",str)
        sql="select * from members where phone=%s"
        cursor.execute(sql,(phone,))
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error found ",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def type():
    con=get_connection()
    if con is None:
        return
    try:
        cursor=con.cursor()
        memtype=safeinput("enter a type",str)
        sql="select * from members where membership=%s"
        cursor.execute(sql,(memtype,))
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error while occuring",e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

# create_db()
# create_table()
while True:
    print("\n\n\t\t\t\twelcome to the vsd gym dude\n\n")
    list="""
1. Add New Member
2. Update Member Details
3. Delete Member
4. View All Members
5. Search Member by Phone
6. View Members by Membership Type
7. Exit
"""
    print(list)
    try:
        opt=int(input("Enter your Choice:"))
    except ValueError as v:
        print("select the value from 1 to 7 ")
    if opt==1:
        newmem()
    elif opt==2:
        update()
    elif opt==3:
        delete()
    elif opt==4:
        view()
    elif opt==5:
        searchbyphone()
    elif opt==6:
        type()
    else:
        print("byeeeeeeee")
        quit()