import employee
import 

def get_file_name():
    filename = input("Enter csv file to add or update employees")
    return filename

def main_menu():
    print("1. Add Employee")
    print("2. Update existing Employee")
    print("3. Remove Employee")
    print("4. List current Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

while True:
    filename = get_file_name()
    ems = ems(filename)
    choice = main_menu()
    if choice == '1':
        firstName = input("Enter your first name:\n")
        lastName = input("Enter your last name:\n")
        salary = input("Enter salary for employee:\n")
        dep = input("Which department?\n")
        emp = employee(firstName, lastName, salary, dep)
        ems.add_New_employee(emp)
    elif choice == '2':
        update = input("Insert Employee ID:\n")
    elif choice == '3':
        remove = input("Enter Employee ID:\n")
    elif choice == '4':
        display = input("Enter Employee ID:\n")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

