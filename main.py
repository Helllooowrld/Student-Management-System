import login_register
import os
from student import Student

os.system("cls" if os.name == "nt" else "clear")
print(
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
    "Welcome to Student Management System",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
)
choice = 0
access = False
while True:
    choice = int(
        input("Please press: \n1 for login.\n2 for registration.\n3 for exiting.\n")
    )
    type(choice)
    if choice == 1:
        print(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
            "Login Screen",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
        )
        login_register.login()
        access = True
        break

    if choice == 2:
        print(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
            "Registration Screen",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
        )
        login_register.register()
        continue

    if choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again")

    os.system("cls" if os.name == "nt" else "clear")
while access:
    print(
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
        "Menu",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
    )
    choice = int(
        input(
            (
                "What would you want to do?\nPress 1 for adding students.\nPress 2 for deleting student from database.\nPress 3 for adding marks to student.\nPress 4 for adding attendance.\nPress 5 for editing student data.\nPress 6 for searching student.\nPress 7 for assigning grades.\nPress 8 for exporting data to another file.\nPress 9 for exiting.\n"
            )
        )
    )
    student = Student(None, None)
    if choice == 1:
        name = input("Enter the full name of the student: ")
        id_no = int(input("Enter the Id no of the student: "))
        student = Student(name, id_no)
        student.add_students()
    elif choice == 2:
        student.delete_student()
    elif choice == 3:
        student.add_marks()
    elif choice == 4:
        student.add_attendance()
    elif choice == 5:
        student.edit_student()
    elif choice == 6:
        search_by = input(
            "Enter the way that you want to search the student. Type:\n'name' for searching students using name.\n'id' for searching student using id.\n'div' for searching student using division.\n"
        )
        result = student.search(search_by)
        print(f"Fetched Results: \n{result}")
    elif choice == 7:
        student.assign_grades()
    elif choice == 8:
        student.export()
    elif choice == 9:
        print("Thank you for using the system. Have a nice day/night!!!:D")
        break
    else: 
        print("Invalid choice")
