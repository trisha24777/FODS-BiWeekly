'''
This program defines a Student class, instantiates an object, takes input for its attributes, and displays the output.
'''
class Student:
    """
    Represents a student with attributes such as id, name, address, admission year, level, and section.
    """
    def __init__(self, id, name, address, admission_year, level, section):
        """
        Initializes a Student object.

        Args:
            id (int): The student's ID.
            name (str): The student's name.
            address (str): The student's address.
            admission_year (int): The year of admission.
            level (str): The student's current level/grade.
            section (str): The student's section/class.
        """
        self.id = id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display_details(self):
        """
        Displays the details of the student.
        """
        print("\nStudent Details:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

if __name__ == "__main__":
    try:
        student_id = int(input("Enter student ID: "))
        student_name = input("Enter student name: ")
        student_address = input("Enter student address: ")
        admission_year = int(input("Enter admission year: "))
        student_level = input("Enter student level: ")
        student_section = input("Enter student section: ")

        student1 = Student(student_id, student_name, student_address, admission_year, student_level, student_section)
        student1.display_details()

    except ValueError:
        print("Invalid input. Please enter a valid integer for ID and admission year.")
    except Exception as e:
        print(f"An error occurred: {e}")