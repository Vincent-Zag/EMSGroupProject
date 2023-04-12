import ems
import employee
import CSVWriter

def main_menu():
    print("1. Add Employee")
    print("2. Update existing Employee")
    print("3. Remove Employee")
    print("4. List current Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def NameError(firstname, lastname):
    if firstname.isalpha() or lastName.isalpha() == False:
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
    if option > 5 or option < 1:
        print("invalid option")

if __name__=='__main__':
    while True:
        choice = main_menu()
        try:
            if choice == '1':
                try:
                    firstName = input("Enter first name:\n")
                    lastName = input("Enter last name:\n")
                    salary = input("Enter salary for employee:\n")
                    dep = input("Which department?\n")

                    if NameError(firstName, lastName):
                        print("...name is A-Okay")

                        #ems.addNewEmployee(firstName, lastName, salary, dep, employee.create_id())
                except:
                    print("error")
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
        except:
            InvOption(choice)
