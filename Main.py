class University:
    def __init__(self, name):
        self.name = University
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def display_departments(self):
        for department in self.departments:
            print(department)


from university import University # type: ignore

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

from Human import Human

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

from teacher import Teacher # type: ignore

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

from Human import Human

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


from student import Student # type: ignore

class Section:
    def __init__(self, section_name, teacher):
        self.section_name = section_name
        self.teacher = teacher
        self.students = []
        self.schedule = None

    def add_student(self, student):
        self.students.append(student)

    def set_schedule(self, schedule):
        self.schedule = schedule

    def display_info(self):
        print(f"Section: {self.section_name}")
        print(f"Teacher: {self.teacher.name}")
        print("Students in the section:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")
        print(f"Schedule: {self.schedule}")


from section import Section # type: ignore

class Schedule:
    def __init__(self, day, time):
        self.day = day
        self.time = time

    def __str__(self):
        return f"{self.day} at {self.time}"

from schedule import Schedule # type: ignore

# Create a university
uni = University("Tech University")

# Create a teacher and a section
teacher = Teacher("Dr. Smith", 45, "Mathematics")
section = Section("Math 101", teacher)

# Create students and add them to the section
student1 = Student("Alice", 20, "S123")
student2 = Student("Bob", 22, "S124")

section.add_student(student1)
section.add_student(student2)

# Create and set a schedule for the section
schedule = Schedule("Monday", "10:00 AM - 12:00 PM")
section.set_schedule(schedule)

# Display section details
section.display_info()
