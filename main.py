import login_register

print("Welcome to Student Management System")
choice=int(input("Please choose: \n1 for login.\n2 for registration.\n 3 for exiting"))

while choice!=3:
    login_register.login()