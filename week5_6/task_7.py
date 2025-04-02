'''
This program implements an Employee class, allows input for multiple employees,
writes their details to 'employees.csv', and allows the user to view the list.
'''
import csv

class Employee:
    """
    Represents an employee with attributes such as empid, name, address, contact_number,
    spouse name, number_of_child, and salary.
    """
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        """
        Initializes an Employee object.
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
        Returns the employee details as a list.
        """
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

def add_employee():
    """
    Takes input from the user to create a new Employee object.
    """
    try:
        empid = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        address = input("Enter employee address: ")
        contact_number = input("Enter employee contact number: ")
        spouse_name = input("Enter employee spouse name (if any, else leave blank): ")
        num_children_str = input("Enter the number of children: ")
        number_of_child = int(num_children_str) if num_children_str else 0
        salary = float(input("Enter employee salary: "))
        return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
    except ValueError:
        print("Invalid input. Please enter valid numeric values for ID, number of children, and salary.")
        return None
    except Exception as e:
        print(f"An error occurred during employee input: {e}")
        return None

def write_employees_to_csv(employees, filename="employees.csv"):
    """
    Writes a list of Employee objects to a CSV file.
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["EmpID", "Name", "Address", "Contact", "Spouse", "Children", "Salary"]) # Write header
            for emp in employees:
                writer.writerow(emp.get_details())
        print(f"Employee data written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

def read_employees_from_csv(filename="employees.csv"):
    """
    Reads employee data from the CSV file and returns a list of lists.
    """
    employees_data = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader, None) # Skip header
            if header:
                for row in reader:
                    employees_data.append(row)
        return employees_data
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading from CSV: {e}")
        return []

def display_employees(employees_data):
    """
    Displays the list of employees and their details.
    """
    if not employees_data:
        print("No employee data available.")
        return

    print("\nEmployee Details:")
    print("-" * 80)
    print(f"{'EmpID':<10}{'Name':<20}{'Address':<30}{'Contact':<15}{'Spouse':<15}{'Children':<10}{'Salary':<10}")
    print("-" * 80)
    for emp in employees_data:
        print(f"{emp[0]:<10}{emp[1]:<20}{emp[2]:<30}{emp[3]:<15}{emp[4]:<15}{emp[5]:<10}{emp[6]:<10}")
    print("-" * 80)

if __name__ == "__main__":
    employees = []
    while True:
        print("\nEmployee Management System")
        print("1. Add New Employee")
        print("2. View Employee List")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_employee = add_employee()
            if new_employee:
                employees.append(new_employee)
                write_employees_to_csv(employees)
        elif choice == '2':
            employee_data = read_employees_from_csv()
            display_employees(employee_data)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")