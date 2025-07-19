import login_register
import os

os.system("cls" if os.name == "nt" else "clear")
print(
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
    "Welcome to Student Management System",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
)
choice = 0

while True:
    choice = int(
        input("Please press: \n1 for login.\n2 for registration.\n3 for exiting.\n")
    )
    type(choice)
    if choice == 1:
        print(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
            "Login Screen",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
        )
        login_register.login()
        break

    if choice == 2:
        print(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
            "Registration Screen",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" * 2,
        )
        login_register.register()
        break

    if choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again")
