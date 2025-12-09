from db.connection import get_connection
from models.enrollment import Enrollment

def enroll_student():
    con = get_connection()
    if not con:
        return
    try:
        cursor = con.cursor()

        student_id = int(input("Student ID: "))
        cursor.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
        if not cursor.fetchone():
            print("Student not found")
            return

        course_id = int(input("Course ID: "))
        cursor.execute("SELECT * FROM courses WHERE course_id=%s", (course_id,))
        course = cursor.fetchone()
        if not course:
            print("Course not found")
            return

        # check capacity
        cursor.execute("SELECT COUNT(*) FROM enrollments WHERE course_id=%s AND status='Active'", (course_id,))
        count = cursor.fetchone()[0]
        if count >= course[4]:
            print("Course is full")
            return

        enrollment = Enrollment(student_id, course_id)

        sql = "INSERT INTO enrollments(student_id,course_id,enroll_date,status) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, enrollment.to_tuple())
        con.commit()
        print("Enrollment successful")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        con.close()
