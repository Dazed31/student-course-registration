from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

   
    # STUDENT FUNCTIONS
    

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

        if name == "":
            print("Name cannot be empty")
            return

        if "@" not in email:
            print("Invalid email")
            return

        if phone == "":
            print("Phone number cannot be empty")
            return

        new_student = Student(student_id, name, email, phone)
        self.students.append(new_student)

        print("Student added successfully")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found")
            return

        for student in self.students:
            student.display()
            print()

    
    # COURSE FUNCTIONS
   

    def add_course(self):
        course_id = input("Course ID: ")

        if course_id == "":
            print("Course ID cannot be empty")
            return

        for course in self.courses:
            if course.course_id == course_id:
                print("Course ID already exists")
                return

        course_name = input("Course Name: ")
        trainer_name = input("Trainer Name: ")
        capacity = input("Capacity: ")

        if course_name == "":
            print("Course name cannot be empty")
            return

        if trainer_name == "":
            print("Trainer name cannot be empty")
            return

        try:
            capacity = int(capacity)
            if capacity <= 0:
                print("Capacity must be greater than 0")
                return
        except ValueError:
            print("Capacity must be a number")
            return

        new_course = Course(course_id, course_name, trainer_name, capacity)
        self.courses.append(new_course)

        print("Course added successfully")

    def view_courses(self):
        if len(self.courses) == 0:
            print("No courses found")
            return

        for course in self.courses:
            course.display()
            print()