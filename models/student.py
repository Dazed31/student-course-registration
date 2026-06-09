class Student:
    def __init__(self, student_id, name, email, phone_number):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number}")