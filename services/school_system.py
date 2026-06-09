import json
from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []  # stores {"student_id": "", "course_id": ""}

    # ---------------- STUDENTS ----------------
    def add_student(self):
        student_id = input("Student ID: ")

        if not student_id:
            print("Student ID cannot be empty")
            return

        for s in self.students:
            if s.student_id == student_id:
                print("Student already exists")
                return

        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        if not name:
            print("Name cannot be empty")
            return

        if "@" not in email:
            print("Invalid email")
            return

        self.students.append(Student(student_id, name, email, phone))
        print("Student added successfully")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found")
            return

        for s in self.students:
            s.display()
            print()

    # ---------------- COURSES ----------------
    def add_course(self):
        course_id = input("Course ID: ")

        if not course_id:
            print("Course ID cannot be empty")
            return

        for c in self.courses:
            if c.course_id == course_id:
                print("Course already exists")
                return

        course_name = input("Course Name: ")
        trainer_name = input("Trainer Name: ")
        capacity = input("Capacity: ")

        try:
            capacity = int(capacity)
            if capacity <= 0:
                print("Capacity must be greater than 0")
                return
        except ValueError:
            print("Capacity must be a number")
            return

        self.courses.append(Course(course_id, course_name, trainer_name, capacity))
        print("Course added successfully")

    def view_courses(self):
        if len(self.courses) == 0:
            print("No courses found")
            return

        for c in self.courses:
            c.display()
            print()

    # ---------------- REGISTRATION ----------------
    def register_student(self):
        student_id = input("Student ID: ")
        course_id = input("Course ID: ")

        student = None
        course = None

        for s in self.students:
            if s.student_id == student_id:
                student = s

        for c in self.courses:
            if c.course_id == course_id:
                course = c

        if not student or not course:
            print("Student or Course not found")
            return

        # check duplicate
        for r in self.registrations:
            if r["student_id"] == student_id and r["course_id"] == course_id:
                print("Student already registered for this course")
                return

        # check capacity
        count = 0
        for r in self.registrations:
            if r["course_id"] == course_id:
                count += 1

        if count >= course.capacity:
            print("Registration failed. Course is full")
            return

        self.registrations.append({
            "student_id": student_id,
            "course_id": course_id
        })

        print(f"{student.name} successfully registered for {course.course_name}")

    def view_students_in_course(self):
        course_id = input("Course ID: ")

        for r in self.registrations:
            if r["course_id"] == course_id:
                for s in self.students:
                    if s.student_id == r["student_id"]:
                        s.display()
                        print()

    def view_courses_for_student(self):
        student_id = input("Student ID: ")

        for r in self.registrations:
            if r["student_id"] == student_id:
                for c in self.courses:
                    if c.course_id == r["course_id"]:
                        print(c.course_name)

    # ---------------- SAVE / LOAD ----------------
    def save_data(self):
        with open("students.json", "w") as f:
            json.dump([s.__dict__ for s in self.students], f)

        with open("courses.json", "w") as f:
            json.dump([c.__dict__ for c in self.courses], f)

        with open("registrations.json", "w") as f:
            json.dump(self.registrations, f)

        print("Data saved")

    def load_data(self):
        try:
            with open("students.json", "r") as f:
                self.students = [Student(**s) for s in json.load(f)]

            with open("courses.json", "r") as f:
                self.courses = [Course(**c) for c in json.load(f)]

            with open("registrations.json", "r") as f:
                self.registrations = json.load(f)

            print("Data loaded")

        except FileNotFoundError:
            print("No saved data found")