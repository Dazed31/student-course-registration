from services.school_system import SchoolSystem

system = SchoolSystem()


while True:
    print("\n===== Student Course Registration System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View Students in a Course")
    print("8. View Courses for a Student")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        system.add_course()

    elif choice == "5":
        system.view_courses()

    elif choice == "6":
        system.register_student()

    elif choice == "7":
        system.view_students_in_course()

    elif choice == "8":
        system.view_courses_for_student()

    elif choice == "0":
        print("Saving and exiting...")
        break

    else:
        print("Invalid option. Try again.")