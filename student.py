import json
import os

filepath = "./students.json"


class Student:
    """class for student object"""

    def __init__(self, name, id_no):
        self.__name = None
        self.__id_no = None

    def add_students(self) -> None:
        """adds student to the database

        Returns:
          _type_: None
        """
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
                        raise ValueError("Non-unique Id no")

            student_dict["id_no"] = self.__id_no
            student_dict["name"] = self.__name
            imported_data.append(student_dict)
            with open(filepath, "w") as file:
                json.dump(imported_data, file)
            print("Student successfully added to the database.")
        except Exception as e:
            print(f"Error: {e}. Please try again with a unique Id no.")

    def delete_student(self) -> None:
        """deletes the student database stored in a JSON file

        Returns:
        _type_: None
        """
        try:
            delete_id = int(
                input("Enter the Id no of the student that you want to delete: ")
            )
        except Exception as e:
            print(f"Error: {e}. Enter valid Id no.")
            return
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
                            f"Student with Id no.{delete_id} successfully deleted from the database."
                        )
                        success = True
                i += 1
            if not success:
                print("Id not found")

        with open(filepath, "w") as file:
            json.dump(imported_data, file)

    def edit_student(self, add_field=None) -> None:
        """adds/edits the student database like name, Id no., subject, marks, attendance

        Args:
            add_field (str, optional): name of field that i to be added. Defaults to None.

        Returns:
        _type_: None
        """
        success=False
        try:
            edit_id = int(
            input("Enter the Id no of the student whose record you want to add/edit: ")
            )
        except Exception as e:
            print(f"Error: {e}")
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        edit_field = None
        try:
            for data in imported_data:
                for key, value in data.items():
                    if key == "id_no" and value == edit_id:
                        if add_field is None:
                            edit_field = input(
                                "Enter the field that you want to add/edit: "
                            ).capitalize()
                        if edit_field == "Name":
                            self.__name = input("Enter new full name: ")
                            data["name"] = self.__name
                            print(f"{edit_field} successfully edited.")
                            success=True

                        elif edit_field == "Id":
                            self.__id_no = int(input("Enter new Id: "))
                            data["id_no"] = self.__id_no
                            print(f"{edit_field} successfully edited.")
                            success=True

                        elif edit_field == "Marks" or add_field == "Marks":
                            edit_field = add_field
                            subject = input("Enter new subject name: ").lower()
                            obtained_marks = int(input("Enter the obtained marks: "))
                            data["marks"][subject] = obtained_marks
                            print(f"{edit_field} successfully edited.")
                            success=True
                        elif edit_field == "Attendance" or add_field == "Attendance":
                            edit_field = add_field
                            attendance = float(input("Enter the attendance percent: "))
                            data["attendance_percent"] = attendance
                            print(f"{edit_field} successfully edited.")
                            success=True

                        else:
                            raise ValueError("Incorrect field")
                    if not success:
                        raise ValueError("Incorrect Id")

        except Exception as e:
            print(f"Error: {e}. Please try again with correct one.")

        with open(filepath, "w") as file:
            json.dump(imported_data, file)

    def add_marks(self) -> None:
        """adds marks to the student database
         Returns:
        _type_: None
        """
        self.edit_student("Marks")

    def add_attendance(self) -> None:
        """adds attendance percent to student database
        Returns:
        _type_: None
        """
        self.edit_student("Attendance")

    def search_by_name(self) -> list:
        """searches students with the name specified by the user

        Returns:
            list: list of found results
        """
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

    def search_by_id(self) -> dict:
        """searches students with the id no. specified by the user


        Returns:
            dict: dictionary with all the information of the found result
        """
        i = 0
        search_id = int(input("Enter the Id no of the student you want to search: "))
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        for data in imported_data:
            for key, value in data.items():
                if key == "id_no" and value == search_id:
                    return imported_data[i]
            i += 1

    def search_by_div(self) -> list:
        """searches students with the division specified by the user


        Returns:
            list: list of found results
        """ 
        i = 0
        searched_data = []
        search_division = input(
            "Enter the division of student you want to search('dist','first','second','third','failed'): "
        ).lower()
        with open(filepath, "r") as file:
            imported_data = json.load(file)
        for data in imported_data:
            for key, value in data.items():
                if key == "division" and value == search_division:
                    searched_data.append(imported_data[i])
            i += 1
        return searched_data

    def search(self, choice:str):
        """searches students with the name,division or id no. specified by the user

        Args:
            choice (str): searching type(name or id or div)

        Returns:
            _type_:list or dict
        """
        result = []
        if choice == "name":
            result = self.search_by_name()
        elif choice == "id":
            result = self.search_by_id()
        elif choice == "div":
            result = self.search_by_div()
        else:
            print("Incorrect input.")
        return result

    def assign_grades(self)-> None:
        """calculates percentage and assigns grade according to obtained percentage

        Returns:
          _type_: None
        """
        with open(filepath, "r") as file:
            imported_data = json.load(file)
            i = 0

        try:
            for data in imported_data:
                total = 0.0
                length = 0
                for key, value in data.items():
                    if key == "marks":
                        for marks in value.values():
                            length = len(value)
                            total = total + marks
                        if length == 0:
                            raise ValueError(
                                f"One of the marks field of the student with Id no.{imported_data[i]['id_no']} is missing"
                            )
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
                i += 1
        except Exception as e:
            print(f"Error: {e}. Please try again after adding marks.")
        with open(filepath, "w") as file:
            json.dump(imported_data, file)
        print("Grades successfully assigned.")

    def export(self)->None:
        """exports the student database to a new file
        Returns:
          _type_: None
        """

        filename = input("Enter filename: ").split('.')
        filename_proccesed = filename[0]+ ".json"
        choose = input(
            "Do you want to export on the basis of grades obtained by the students?(Y/N): "
        ).capitalize()

        if choose == "Y":
            result = self.search_by_div()
            with open(filename_proccesed, "w") as file:
                json.dump(result, file)
        elif choose == "N":
            with open(filepath, "r") as file:
                imported_data = json.load(file)
            with open(filename_proccesed, "w") as file:
                json.dump(imported_data, file)
        print(f"Data succesfully exported to {filename_proccesed}.")


if __name__ == "__main__":
    student1 = Student("example", 2322)
    success = student1.add_students()
    print(success)
    if success:
        # student2.add_students()
        student1.edit_student()
        result = student1.search("div")
        student1.assign_grades()
        student1.export()
    # student1.delete_student()
    else:
        print("error")
