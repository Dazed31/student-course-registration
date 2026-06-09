from services.school_system import SchoolSystem


def main():
    school_system = SchoolSystem()

    while True:
        print("\n===== Student Course Registration System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. View Courses")
        print("5. Register Student to Course")
        print("6. Save Data")
        print("7. Load Data")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            school_system.add_student()
        elif choice == "2":
            school_system.view_students()
        elif choice == "3":
            school_system.add_course()
        elif choice == "4":
            school_system.view_courses()
        elif choice == "5":
            school_system.register_student_to_course()
        elif choice == "6":
            school_system.save_data()
        elif choice == "7":
            school_system.load_data()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")


main()