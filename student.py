import json
import os

filepath = "./students.json"


class Student:
    def __init__(self, name, id_no):
        self.__name = name
        self.__id_no = id_no

    def add_students(self):
        imported_data = []
        student_dict = {
            "id_no": self.__id_no,
            "name": self.__name,
            "marks": {},
            "attendance_percent": None,
            "obtained_percent": None,
            "division": None,
        }

        with open(filepath, "r") as file:
            imported_data = json.load(file)

        try:
            for data in imported_data:
                for key, value in data.items():
                    if key == "id_no" and value == self.__id_no:
                        raise ValueError("Non-unique Id no.")
        except Exception as e:
            print(f"Error: {e}.")
            return False

        student_dict["id_no"] = self.__id_no
        student_dict["name"] = self.__name
        imported_data.append(student_dict)
        with open(filepath, "w") as file:
            json.dump(imported_data, file)
        print("Student successfully added to the database.")
        return True

    def delete_student(self):
        delete_id = int(
            input("Enter the Id no of the student that you want to delete: ")
        )

        with open(filepath, "r") as file:
            imported_data = json.load(file)
            print(imported_data[0])
            i = 0
            success = False
            for data in imported_data:
                for key, value in data.items():
                    if key == "id_no" and value == delete_id:
                        del imported_data[i]
                        os.system("cls" if os.name == "nt" else "clear")
                        print(
                            f"Student with {delete_id} successfully deleted from the database."
                        )
                        success = True
                i += 1
            if not success:
                print("Id not found")

        with open(filepath, "w") as file:
            json.dump(imported_data, file)

    def edit_student(self):
        edit_id = int(
            input("Enter the Id no of the student whose record you want to edit:")
        )
        with open(filepath, "r") as file:
            imported_data = json.load(file)

        try:
            for data in imported_data:
                for key, value in data.items():
                    if key == "id_no" and value == edit_id:
                        edit_field = input(
                            "Enter the field that you want to edit: "
                        ).capitalize()
                        if edit_field == "Name":
                            self.__name = input("Enter name: ")
                            data["name"] = self.__name
                            print(f"{edit_field} successfully edited.")

                        elif edit_field == "Id":
                            self.__id_no = int(input("Enter Id: "))
                            data["id_no"] = self.__id_no
                            print(f"{edit_field} successfully edited.")

                        elif edit_field == "Marks":
                            subject = input("Enter subject name: ").lower()
                            obtained_marks = int(input("Enter the obtained marks: "))
                            data["marks"][subject] = obtained_marks
                            print(f"{edit_field} successfully edited.")

                        elif edit_field == "Attendance":
                            attendance = float(input("Enter the attendance percent: "))
                            data["attendance_percent"] = attendance
                            print(f"{edit_field} successfully edited.")

                        else:
                            raise ValueError("Incorrect field")

        except Exception as e:
            print(f"Error:{e}")
            return False

        with open(filepath, "w") as file:
            json.dump(imported_data, file)
            return True

    def search_by_name(self):
        i = 0
        searched_data = []
        search_name = input("Enter the name of the student you want to search: ")
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        for data in imported_data:
            for key, value in data.items():
                if key == "name" and value == search_name:
                    searched_data.append(imported_data[i])
            i += 1
            print(searched_data)
        return searched_data

    def search_by_id(self):
        i = 0
        search_id = int(input("Enter the Id no of the student you want to search: "))
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        for data in imported_data:
            for key, value in data.items():
                if key == "id_no" and value == search_id:
                    return imported_data[i]
            i += 1

    def search_by_div(self):
        i = 0
        searched_data = []
        search_division = input("Enter the division of student you want to search: ")
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        for data in imported_data:
            for key, value in data.items():
                if key == "division" and value == search_division:
                    searched_data.append(imported_data[i])
            i += 1
        return searched_data

    def search(self, choice):
        result = []
        if choice == 1:
            result = self.search_by_name()
        if choice == 2:
            result = self.search_by_id()
        if choice == 3:
            result = self.search_by_div()
        return result

    def assign_grades(self):
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        for data in imported_data:
            total = 0.0
            length = 0
            for key, value in data.items():
                if key == "marks":
                    for marks in value.values():
                        length = len(value)
                        total = total + marks
                    percent = (total / (length * 100)) * 100
                    data["obtained_percent"] = percent
                    if percent < 40:
                        data["division"] = "failed"
                    elif percent >= 40 and percent < 50:
                        data["division"] = "third"
                    elif percent >= 50 and percent < 65:
                        data["division"] = "second"
                    elif percent >= 65 and percent < 80:
                        data["division"] = "first"
                    else:
                        data["division"] = "dist"

        with open(filepath, "w") as file:
            json.dump(imported_data, file)

    def export(self):
        filename=input("Enter filename: ")
        filename=filename+".json"
        choose=input("Do you want to export on the basis of grades obtained by the students?(Y/N): ").capitalize()

        if choose=="Y":
            result= self.search_by_div()
            with open(filename, "w") as file:
                json.dump(result, file)
        elif choose=="N":
            with open(filepath, "r") as file:
                imported_data = json.load(file)
            with open(filename, "w") as file:
                json.dump(imported_data, file)

if __name__ == "__main__":
    student1 = Student("Aayus Shrestha", 2322)
    # student2= Student("Aayusha Shrestha", 12343)
    success = student1.add_students()
    print(success)
    if success:
        # student2.add_students()
        student1.edit_student()
        result = student1.search(3)
        student1.assign_grades()
        student1.export()
    # student1.delete_student()
    else:
        print("error")
