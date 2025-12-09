import mysql.connector

def create_db():
    try:
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Harinisri2012"
        )
    except:
        print("database not created")
    cursor=con.cursor()
    cursor.execute("create database if not exists hoteldb")
    con.commit()
    
def create_table():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="hoteldb"
    )
    if not con:
        return 
    try:
        cursor=con.cursor()
        sql='''
        create table if not exists students(
        id int auto_increment primary key,
        name varchar(50) not null,
        age int not null,
        room_no varchar(10),
        bed_no varchar(5),
        join_date date not null,
        status varchar(20))
'''
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print("error occur while creating ",e)


def get_connection():
    try:
        con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Harinisri2012",
        database="hoteldb"
        )
        if not con:
            return 
        else:
            print("connected")
            return con
    except:
        print("not connected")

def safeinput(prompt, cast):
    while True:
        try:
            val=cast(input(prompt))
            return val
        except:
            print("enter a valid integer", cast)


def printer(row):
    print("ID | NAME   |  AGE   |  ROOM_NO   |  BED_NO   |  JOIN_DATE  |   STATUS")
    for x in row:
        print(f"{x[0]}  |  {x[1]}   |   {x[2]}  |   {x[3]}  |  {x[4]}   |  {x[5]}  |   {x[6]}     ")
def add_student():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        name=safeinput("enter your name : ",str)
        age=safeinput("enter your age : ",int)
        room_no=safeinput("enter your room no : ",str)
        bed_no=safeinput("enter your bed no : ", str)
        join_date=safeinput("enter your joining date (YYYY-MM-DD) : ",str)
        status=safeinput("enter a status (Active / Left)",str)
        datas=(name,age,room_no,bed_no,join_date,status)
        sql="insert into students (name,age,room_no,bed_no,join_date,status) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,datas)
        con.commit()
        print("Student added successfully!!")
    except Exception as e:
        print("error occur while inserting datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def update_student():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        id=safeinput("enter id to update : ", int)
        name=safeinput("enter your name : ",str)
        age=safeinput("enter your age : ",int)
        room_no=safeinput("enter your room no : ",str)
        bed_no=safeinput("enter your bed no : ", str)
        join_date=safeinput("enter your joining date (YYYY-MM-DD) : ",str)
        status=safeinput("enter a status (Active / Left)",str)
        datas=(name,age,room_no,bed_no,join_date,status,id)
        sql="update students set name=%s,age=%s,room_no=%s,bed_no=%s,join_date=%s,status=%s where id=%s"
        cursor.execute(sql,datas)
        con.commit()
        print("Student updated successfully!!")
    except Exception as e:
        print("error occur while updating datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def delete_student():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        id=safeinput("enter id to delete : ", int)
        sql="delete from students where id=%s"
        cursor.execute(sql,(id,))
        con.commit()
        print("Student deleted successfully!!")
    except Exception as e:
        print("error occur while delted datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def view_all_students():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        sql="select * from students"
        cursor.execute(sql)
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error occur while recovering datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def search_by_room():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        room=safeinput("enter room_no to search : ",str)
        sql="select * from students where room_no =%s"
        cursor.execute(sql,(room,))
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error occur while recovering datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def view_active_students():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        sql="select * from students where status=%s"
        cursor.execute(sql,("Active",))
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error occur while recovering datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass

def mark_student_left():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        sql="select * from students where status=%s"
        cursor.execute(sql,("Left",))
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error occur while recovering datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
def upper():
    con=get_connection()
    if not con:
        return
    try:
        cursor=con.cursor()
        sql='''SELECT
    UCASE(name) AS upper_name,*
FROM students;
 '''
        cursor.execute(sql)
        row=cursor.fetchall()
        printer(row)
    except Exception as e:
        print("error occur while recovering datas!!!", e)
    finally:
        try:
            cursor.close()
            con.close()
        except:
            pass
def main():
    while True:
        print("""
1. Add New Student
2. Update Student Details
3. Delete Student
4. View All Students
5. Search Students by Room Number
6. View Only Active Students
7. Mark Student as Left

8. Exit
9.upper the name
              
""")
        try:
            choice = safeinput("Enter your choice: ",int)
        except ValueError:
            print("Please enter a number between 1 and 8")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            update_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            view_all_students()
        elif choice == 5:
            search_by_room()
        elif choice == 6:
            view_active_students()
        elif choice == 7:
            mark_student_left()
        elif choice == 8:
            print("Bye!")
            break
        elif choice==9:
            upper()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    create_db()
    create_table()
    main()
