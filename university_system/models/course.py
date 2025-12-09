class Course:
    def __init__(self, name, department, credits, capacity):
        self.name = name
        self.department = department
        self.credits = credits
        self.capacity = capacity

    def to_tuple(self):
        return (self.name, self.department, self.credits, self.capacity)
