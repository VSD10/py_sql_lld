class Grade:
  
    def __init__(self, grade_id=None, enroll_id=None, assignment_name=None, marks=None, grade=None):
        self.grade_id = grade_id
        self.enroll_id = enroll_id
        self.assignment_name = assignment_name
        self.marks = marks
        self.grade = grade
    
    def to_tuple(self):
        return (self.enroll_id, self.assignment_name, self.marks, self.grade)
    
