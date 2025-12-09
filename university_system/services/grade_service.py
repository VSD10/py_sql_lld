from db.connection import get_connection

def add_marks():
    con = get_connection()
    if not con:
        return
    try:
        cursor = con.cursor()

        enroll_id = int(input("Enrollment ID: "))
        assignment = input("Assignment Name: ")
        marks = int(input("Marks: "))

        # grade calculation
        if marks >= 90: grade = "A"
        elif marks >= 80: grade = "B"
        elif marks >= 70: grade = "C"
        elif marks >= 60: grade = "D"
        else: grade = "F"

        sql = "INSERT INTO grades(enroll_id,assignment_name,marks,grade) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (enroll_id, assignment, marks, grade))
        con.commit()

        print("Marks added")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        con.close()
