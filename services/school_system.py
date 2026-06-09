import json
import os

from models.student import Student
from models.course import Course


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []
        self.data_folder_path = "data"

    # ---------------- ADD STUDENT ----------------
    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        phone_number = input("Enter student phone number: ")

        self.students.append(Student(student_id, name, email, phone_number))
        print("Student added successfully!")

    # ---------------- VIEW STUDENTS ----------------
    def view_students(self):
        for student in self.students:
            print(
                f"{student.student_id} | {student.name} | {student.email} | {student.phone_number}"
            )

    # ---------------- ADD COURSE ----------------
    def add_course(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        trainer_name = input("Enter trainer name: ")
        capacity = int(input("Enter course capacity: "))

        self.courses.append(Course(course_id, course_name, trainer_name, capacity))
        print("Course added successfully!")

    # ---------------- VIEW COURSES ----------------
    def view_courses(self):
        for course in self.courses:
            print(
                f"{course.course_id} | {course.course_name} | {course.trainer_name} | {course.capacity}"
            )

    # ---------------- REGISTER STUDENT ----------------
    def register_student_to_course(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        # prevent duplicate registration
        for registration in self.registrations:
            if registration["student_id"] == student_id and registration["course_id"] == course_id:
                print("Student already registered for this course.")
                return

        # count registrations for course
        registration_count = 0
        for registration in self.registrations:
            if registration["course_id"] == course_id:
                registration_count += 1

        # FIXED LINE (this was your error)
        for course in self.courses:
            if course.course_id == course_id:
                if registration_count >= course.capacity:
                    print("Registration failed. Course is full.")
                    return

        self.registrations.append({
            "student_id": student_id,
            "course_id": course_id
        })

        print("Student successfully registered!")

    # ---------------- SAVE DATA ----------------
    def save_data(self):
        with open(os.path.join(self.data_folder_path, "students.json"), "w") as file:
            json.dump([s.__dict__ for s in self.students], file)

        with open(os.path.join(self.data_folder_path, "courses.json"), "w") as file:
            json.dump([c.__dict__ for c in self.courses], file)

        with open(os.path.join(self.data_folder_path, "registrations.json"), "w") as file:
            json.dump(self.registrations, file)

        print("Data saved successfully!")

    # ---------------- LOAD DATA ----------------
    def load_data(self):
        try:
            with open(os.path.join(self.data_folder_path, "students.json"), "r") as file:
                self.students = [
                    Student(s["student_id"], s["name"], s["email"], s["phone_number"])
                    for s in json.load(file)
                ]

            with open(os.path.join(self.data_folder_path, "courses.json"), "r") as file:
                self.courses = [
                    Course(c["course_id"], c["course_name"], c["trainer_name"], c["capacity"])
                    for c in json.load(file)
                ]

            with open(os.path.join(self.data_folder_path, "registrations.json"), "r") as file:
                self.registrations = json.load(file)

            print("Data loaded successfully!")

        except FileNotFoundError:
            print("No saved data found.")