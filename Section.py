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
