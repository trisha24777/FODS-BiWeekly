'''
This program defines a Student class, instantiates an object, takes input for its attributes, and displays the output.
'''

# Define the Student class
class Student:
    """
    Represents a student with attributes such as id, name, address, admission year, level, and section.
    """
    def __init__(self, id, name, address, admission_year, level, section):
        """
        Initializes a Student object with the provided attributes.

        Args:
            id (int): The student's ID.
            name (str): The student's name.
            address (str): The student's address.
            admission_year (int): The year the student was admitted.
            level (str): The student's current level/grade.
            section (str): The student's section/class.
        """
        self.id = id                # Store student ID
        self.name = name            # Store student name
        self.address = address      # Store student address
        self.admission_year = admission_year  # Store admission year
        self.level = level          # Store student level/grade
        self.section = section      # Store student section/class

    def display_details(self):
        """
        Displays the details of the student.
        This method prints all the attributes of the student object.
        """
        print("\nStudent Details:")
        print(f"ID: {self.id}")              # Print student ID
        print(f"Name: {self.name}")          # Print student name
        print(f"Address: {self.address}")    # Print student address
        print(f"Admission Year: {self.admission_year}")  # Print admission year
        print(f"Level: {self.level}")        # Print student level/grade
        print(f"Section: {self.section}")    # Print student section/class

# Main block that runs when the script is executed
if __name__ == "__main__":
    try:
        # Take input from the user for student attributes
        student_id = int(input("Enter student ID: "))  # Convert ID to integer
        student_name = input("Enter student name: ")   # Take student name input
        student_address = input("Enter student address: ")  # Take student address input
        admission_year = int(input("Enter admission year: "))  # Convert admission year to integer
        student_level = input("Enter student level: ")  # Take student level input
        student_section = input("Enter student section: ")  # Take student section input

        # Create a Student object with the user inputs
        student1 = Student(student_id, student_name, student_address, admission_year, student_level, student_section)

        # Display the details of the created student
        student1.display_details()

    except ValueError:
        # Handle case when the user inputs an invalid integer for ID or admission year
        print("Invalid input. Please enter a valid integer for ID and admission year.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
