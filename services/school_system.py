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
        student_id = input("Enter student identification number: ")
        student_name = input("Enter student full name: ")
        student_email = input("Enter student email address: ")
        student_phone_number = input("Enter student phone number: ")

        new_student = Student(student_id, student_name, student_email, student_phone_number)
        self.students.append(new_student)

        print("Student added successfully!")

    # ---------------- VIEW STUDENTS ----------------
    def view_students(self):
        for student in self.students:
            print(
                f"Student ID: {student.student_id}, "
                f"Name: {student.name}, "
                f"Email: {student.email}, "
                f"Phone Number: {student.phone_number}"
            )

    # ---------------- ADD COURSE ----------------
    def add_course(self):
        course_id = input("Enter course identification number: ")
        course_name = input("Enter course name: ")
        trainer_name = input("Enter trainer full name: ")
        course_capacity = int(input("Enter course capacity: "))

        new_course = Course(course_id, course_name, trainer_name, course_capacity)
        self.courses.append(new_course)

        print("Course added successfully!")

    # ---------------- VIEW COURSES ----------------
    def view_courses(self):
        for course in self.courses:
            print(
                f"Course ID: {course.course_id}, "
                f"Course Name: {course.course_name}, "
                f"Trainer Name: {course.trainer_name}, "
                f"Course Capacity: {course.course_capacity}"
            )

    # ---------------- REGISTER STUDENT ----------------
    def register_student_to_course(self):
        student_id = input("Enter student identification number: ")
        course_id = input("Enter course identification number: ")

        # prevent duplicate registration
        for registration in self.registrations:
            if registration["student_id"] == student_id and registration["course_id"] == course_id:
                print("This student is already registered for this course.")
                return

        # check course capacity
        registration_count = 0
        for registration in self.registrations:
            if registration["course_id"] == course_id:
                registration_count += 1

        for course in self.courses:
            if course.course_id == course_id:
                if registration_count >= course.course_capacity:
                    print("Registration failed. This course is already full.")
                    return

        self.registrations.append({
            "student_id": student_id,
            "course_id": course_id
        })

        print("Student successfully registered for course!")

    # ---------------- SAVE DATA ----------------
    def save_data(self):
        students_file_path = os.path.join(self.data_folder_path, "students.json")
        courses_file_path = os.path.join(self.data_folder_path, "courses.json")
        registrations_file_path = os.path.join(self.data_folder_path, "registrations.json")

        with open(students_file_path, "w") as students_file:
            json.dump([student.__dict__ for student in self.students], students_file)

        with open(courses_file_path, "w") as courses_file:
            json.dump([course.__dict__ for course in self.courses], courses_file)

        with open(registrations_file_path, "w") as registrations_file:
            json.dump(self.registrations, registrations_file)

        print("Data saved successfully!")

    # ---------------- LOAD DATA ----------------
    def load_data(self):
        try:
            students_file_path = os.path.join(self.data_folder_path, "students.json")
            courses_file_path = os.path.join(self.data_folder_path, "courses.json")
            registrations_file_path = os.path.join(self.data_folder_path, "registrations.json")

            with open(students_file_path, "r") as students_file:
                students_data = json.load(students_file)
                self.students = []

                for student_data in students_data:
                    self.students.append(
                        Student(
                            student_data["student_id"],
                            student_data["name"],
                            student_data["email"],
                            student_data["phone_number"]
                        )
                    )

            with open(courses_file_path, "r") as courses_file:
                courses_data = json.load(courses_file)
                self.courses = []

                for course_data in courses_data:
                    self.courses.append(
                        Course(
                            course_data["course_id"],
                            course_data["course_name"],
                            course_data["trainer_name"],
                            course_data["course_capacity"]
                        )
                    )

            with open(registrations_file_path, "r") as registrations_file:
                self.registrations = json.load(registrations_file)

            print("Data loaded successfully!")

        except FileNotFoundError:
            print("No saved data found in the data folder.")