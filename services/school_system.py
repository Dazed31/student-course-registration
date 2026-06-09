from models.student import Student


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

    def add_student(self):
        student_id = input("Student ID: ")

        if student_id == "":
            print("Student ID cannot be empty")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists")
                return

        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        if "@" not in email:
            print("Invalid email")
            return

        student = Student(student_id, name, email, phone)

        self.students.append(student)

        print("Student added successfully")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found")
            return

        for student in self.students:
            student.display()
            print()