import csv

class Employee:
    """
    Represents an employee with attributes such as empid, name, address, contact_number,
    spouse name, number_of_child, and salary.
    """
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        """
        Initializes an Employee object with the provided attributes.

        Args:
            empid (int): The employee's ID.
            name (str): The employee's name.
            address (str): The employee's address.
            contact_number (str): The employee's contact number.
            spouse_name (str): The employee's spouse name (if applicable).
            number_of_child (int): The number of children the employee has.
            salary (float): The employee's salary.
        """
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def get_details(self):
        """
        Returns the employee details as a list, which can be written to a CSV.

        Returns:
            list: A list containing employee details.
        """
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

def add_employee():
    """
    Takes input from the user to create a new Employee object.
    
    Returns:
        Employee: A new Employee object or None if input is invalid.
    """
    try:
        # Prompt user for employee information
        empid = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        address = input("Enter employee address: ")
        contact_number = input("Enter employee contact number: ")
        spouse_name = input("Enter employee spouse name (if any, else leave blank): ")
        num_children_str = input("Enter the number of children: ")
        number_of_child = int(num_children_str) if num_children_str else 0
        salary = float(input("Enter employee salary: "))
        
        # Return the new Employee object
        return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
    except ValueError:
        # Handle case where input is not a valid integer or float
        print("Invalid input. Please enter valid numeric values for ID, number of children, and salary.")
        return None
    except Exception as e:
        # Handle any other exceptions that may occur during employee input
        print(f"An error occurred during employee input: {e}")
        return None

def write_employees_to_csv(employees, filename="employees.csv"):
    """
    Writes a list of Employee objects to a CSV file.
    
    Args:
        employees (list): List of Employee objects to be written.
        filename (str): The name of the CSV file (default is 'employees.csv').
    """
    try:
        # Open the CSV file in write mode
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write the header row to the CSV file
            writer.writerow(["EmpID", "Name", "Address", "Contact", "Spouse", "Children", "Salary"])
            
            # Write the details of each employee
            for emp in employees:
                writer.writerow(emp.get_details())
        
        # Notify the user that the data has been written successfully
        print(f"Employee data written to '{filename}' successfully.")
    except Exception as e:
        # Handle any errors that occur during the file writing process
        print(f"An error occurred while writing to CSV: {e}")

def read_employees_from_csv(filename="employees.csv"):
    """
    Reads employee data from the CSV file and returns a list of lists.
    
    Args:
        filename (str): The name of the CSV file (default is 'employees.csv').
    
    Returns:
        list: A list of lists containing employee data.
    """
    employees_data = []
    try:
        # Open the CSV file in read mode
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None) # Skip header row
            
            # Read each row and append it to the list of employees' data
            if header:
                for row in reader:
                    employees_data.append(row)
        
        # Return the list of employees' data
        return employees_data
    except FileNotFoundError:
        # Handle case where the file doesn't exist
        print(f"Error: '{filename}' not found.")
        return []
    except Exception as e:
        # Handle any other errors that occur during the file reading process
        print(f"An error occurred while reading from CSV: {e}")
        return []

def display_employees(employees_data):
    """
    Displays the list of employees and their details.
    
    Args:
        employees_data (list): List of employee data to be displayed.
    """
    if not employees_data:
        # Handle case where no employee data is available
        print("No employee data available.")
        return

    # Display the column headers
    print("\nEmployee Details:")
    print("-" * 80)
    print(f"{'EmpID':<10}{'Name':<20}{'Address':<30}{'Contact':<15}{'Spouse':<15}{'Children':<10}{'Salary':<10}")
    print("-" * 80)

    # Display each employee's data
    for emp in employees_data:
        print(f"{emp[0]:<10}{emp[1]:<20}{emp[2]:<30}{emp[3]:<15}{emp[4]:<15}{emp[5]:<10}{emp[6]:<10}")
    
    print("-" * 80)

if __name__ == "__main__":
    employees = []
    while True:
        # Display menu options
        print("\nEmployee Management System")
        print("1. Add New Employee")
        print("2. View Employee List")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new employee and write to the CSV file
            new_employee = add_employee()
            if new_employee:
                employees.append(new_employee)
                write_employees_to_csv(employees)
        elif choice == '2':
            # Read employees from the CSV and display them
            employee_data = read_employees_from_csv()
            display_employees(employee_data)
        elif choice == '3':
            # Exit the program
            print("Exiting the system.")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")
