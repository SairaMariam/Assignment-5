from University import University 

from Human import Human

from Teacher import Teacher 

from Human import Human

from Student import Student 

from Section import Section 

from Schedule import Schedule 

# Create a university
uni = University("Tech University")

# Create a teacher and a section
teacher = Teacher("Sir. Abu Huraira", 45, "Generative Al Engineering")
section = Section("Batch 65", teacher)

# Create students and add them to the section
student1 = Student("Saira", 20, "PIAIC250077")
student2 = Student("Maryam", 22, "PIAIC250078")

section.add_student(student1)
section.add_student(student2)

# Create and set a schedule for the section
schedule = Schedule("Sunday", "02:00 PM - 06:00 PM")
section.set_schedule(schedule)

# Display section details
section.display_info()
