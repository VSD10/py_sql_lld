from db.connection import get_connection
from models.student import Student

def add_student():
    con = get_connection()
    if not con:
        return
    try:
        name = input("Name: ")
        email = input("Email: ")
        year = int(input("Year (1-4): "))
        major = input("Major: ")

        student = Student(name, email, year, major)

        cursor = con.cursor()
        sql = "INSERT INTO students(name,email,year,major) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, student.to_tuple())
        con.commit()
        print("Student added successfully")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        con.close()
