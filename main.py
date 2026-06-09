from services.school_system import SchoolSystem


def main():
    system = SchoolSystem()

    while True:
        print("\n===== Student Course Registration System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. View Courses")
        print("5. Register Student to Course")
        print("6. View Students in Course")
        print("7. View Courses for Student")
        print("8. Save Data")
        print("9. Load Data")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            system.add_course()

        elif choice == "4":
            system.view_courses()

        elif choice == "5":
            system.register_student()

        elif choice == "6":
            system.view_students_in_course()

        elif choice == "7":
            system.view_courses_for_student()

        elif choice == "8":
            system.save_data()

        elif choice == "9":
            system.load_data()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()