from datetime import datetime

class Enrollment:
    def __init__(self, student_id, course_id, status="Active"):
        self.student_id = student_id
        self.course_id = course_id
        self.enroll_date = datetime.now().strftime("%Y-%m-%d")
        self.status = status

    def to_tuple(self):
        return (self.student_id, self.course_id, self.enroll_date, self.status)
