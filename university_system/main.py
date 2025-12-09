from services.student_service import add_student
from services.course_service import add_course
from services.enrollment_service import enroll_student
from services.grade_service import add_marks

def main():
    while True:
        print("""
1. Add Student
2. Add Course
3. Enroll Student
4. Add Marks
5. Exit
""")
        ch = input("Enter choice: ")

        if ch == "1": add_student()
        elif ch == "2": add_course()
        elif ch == "3": enroll_student()
        elif ch == "4": add_marks()
        elif ch == "5":
            print("Bye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
