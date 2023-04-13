from ems import ems
from employee import Employee
from CSVWriter import CSVWriter

def getFileName():
    fileName = input("Enter csv file name where you want to update or create employees: ")
    return fileName

def main_menu():
    print("1. Add Employee")
    print("2. Update existing Employee")
    print("3. Remove Employee")
    print("4. List current Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def NameError(firstName, lastName):
    if firstName.isalpha() == False or lastName.isalpha() == False:
        print("Name has to have letters only, you cannot have special characters or numbers in your name")
        return False
    else:
        return True 
    
def InvSalary(salary):
    if salary > 80000:
        print("Employee max salary is 80000")
    elif salary < 30000:
        print("please dont be cheap minimum wage is 30000 here")
    else:
        print("salary has to be a integer")

def InvOption(option):
    option = int(option)
    if option > 5 or option < 1:
        print("invalid option")

if __name__=='__main__':
    filename = getFileName()
    system = ems(filename)
    while True:
        choice = main_menu()
        try:
            if choice == '1':
                firstName = input("Enter first name:\n")
                lastName = input("Enter last name:\n")
                salary = input("Enter salary for employee:\n")
                dep = input("Which department?\n")
                if NameError(firstName, lastName):
                    print("...name is A-Okay")
                emp = Employee(firstName, lastName, salary, dep)
                system.add_New_Employee(emp)
            elif choice == '2':
                update = input("Insert Employee ID:\n")
                system.update_Employee(update, firstname="asd")
            elif choice == '3':
                remove = input("Enter Employee ID:\n")
            elif choice == '4':
                display = input("Enter Employee ID:\n")
                system.list_Emp_Info(display)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except:
            InvOption(choice)