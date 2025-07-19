import json
import os

filepath = "./credentials.json"


def check_email(email:str)->None:
    """checks whether the entered email is correct or not. The email should contai only one '@' and should either end with 'gmail.com' or 'hotmail.com' or 'college_name.edu.np'

    Args:
        email (str):email through which the user can register or login into the system

    Returns:
        _type_: None
    """
    split_email_by_dot = email.split(".")
    split_email_by_at = email.split("@")

    try:
        if len(split_email_by_at) == 2:
            if len(split_email_by_dot) == 3:
                if (
                    (split_email_by_dot[1] != "edu" and split_email_by_dot[2] != "np")
                    or split_email_by_at[0] == ""
                    or split_email_by_at[1] == "gmail.edu.np"
                    or split_email_by_at[1] == "hotmail.edu.np"
                ):
                    raise ValueError("Invalid email.")
            elif len(split_email_by_dot) == 2:
                if (
                    split_email_by_at[1] != "gmail.com"
                    and split_email_by_at[1] != "hotmail.com"
                ) or split_email_by_at[0] == "":
                    raise ValueError("Invalid email.")
            else:
                raise ValueError("Invalid email.")
        else:
            raise ValueError("Invalid email.")
    except Exception as e:
        print(f"Error: {e}\nPlease try again.")


def login()->None:
    """checks whether the entered credentials are valid or not

    Returns:
        _type_: None
    """
    while True:
        i = 0
        success = "No"
        email = input("Enter a valid email: ")
        if check_email(email) == "Failure":
            continue
        password = input("Enter your password: ")

        try:
            with open(filepath, "r") as file:
                database = json.load(file)
                if database == []:
                    raise ValueError("No database. Please wait while we work on it.")

            for data in database:
                for key, value in data.items():
                    if key == "email":
                        if value == email:
                            if database[i]["password"] != password:
                                raise ValueError("Invalid email or password.")
                            else:
                                os.system("cls" if os.name == "nt" else "clear")
                                print("Login successful...")
                                print(f"Welcome {database[i]['name']}!!!")
                                success = "Yes"
                                break

                i += 1

            if success == "No":
                raise ValueError("Email not registered")

        except Exception as e:
            print(f"Error: {e}\nPlease try again")
            continue
        break


def register()->None:
    """checks whether the entered credentials are correct or not while registering
     
     Returns:
        _type_: None

    """
    while True:
        email = input("Enter a valid email: ")
        if check_email(email) == "Failure":
            continue

        try:
            with open(filepath, "r") as file:
                database = json.load(file)
                if database != []:
                    for data in database:
                        for key, value in data.items():
                            if key == "email":
                                if value == email:
                                    raise ValueError(
                                        f"The email '{email}' has already been registered."
                                    )
            password = input("Enter your password: ")
            retype_password = input("Confirm your password: ")
            if password != retype_password:
                raise ValueError("Invalid password.")
        except Exception as e:
            print(f"Error: {e}")
            continue
        break

    name = input("Enter your name: ")
    credentials_dict = {}
    credentials_dict["email"] = email
    credentials_dict["password"] = password
    credentials_dict["name"] = name
    database.append(credentials_dict)
    with open(filepath, "w") as file:
        json.dump(database, file)
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Registration with {email} successfull.")


if __name__ == "__main__":
    login()
