from services.school_system import SchoolSystem

system = SchoolSystem()

while True:
    print("\n===== Student Course Registration System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. View Courses")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.add_course()

    elif choice == "4":
        system.view_courses()

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option")