class University:
    def __init__(self, name):
        self.name = University
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_departments(self):
        for department in self.departments:
            print(department)
