from db.connection import get_connection
from models.course import Course

def add_course():
    con = get_connection()
    if not con:
        return
    try:
        name = input("Course Name: ")
        dept = input("Department: ")
        credits = int(input("Credits: "))
        capacity = int(input("Capacity: "))

        course = Course(name, dept, credits, capacity)

        cursor = con.cursor()
        sql = "INSERT INTO courses(course_name,department,credits,capacity) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, course.to_tuple())
        con.commit()
        print("Course added successfully")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        con.close()
