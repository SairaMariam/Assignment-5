class Human:
    def __init__(self, name, age):                                                        
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

from Human import Human

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
