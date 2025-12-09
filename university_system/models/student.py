class Student:
    def __init__(self, name, email, year, major):
        self.name = name
        self.email = email
        self.year = year
        self.major = major

    def to_tuple(self):
        return (self.name, self.email, self.year, self.major)
