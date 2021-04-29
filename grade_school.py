class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        return sorted(self.students, key=lambda x: (self.students[x], x))

    def grade(self, grade_number):
        return sorted(filter((lambda x: self.students[x] == grade_number), self.students))
