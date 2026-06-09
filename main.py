from services.school_system import SchoolSystem

system = SchoolSystem()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "0":
        break

    else:
        print("Invalid option")