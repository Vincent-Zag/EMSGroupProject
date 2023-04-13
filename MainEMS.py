from ems import ems
from employee import Employee
from CSVWriter import CSVWriter
import department

def getFileName():
    fileName = input("Enter csv file name where you want to update or create employees: ")
    if fileName[-4:] != '.csv':
        fileName += '.csv'
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
    if int(salary) > 80000:
        print("Employee max salary is 80000")
    elif int(salary) < 30000:
        print("please dont be cheap minimum wage is 30000 here")
    elif type(salary) != int:
        print("Salary has to be a integer")
    else:
        return True
    
def InvOption(option):
    if int(option) > 5 or int(option) < 1:
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
                    Salary = int(input("Enter salary for employee:\n"))
                    dep = input("Which department?\n")
                    if NameError(firstName, lastName):
                        print("...name is A-Okay")
                    if InvSalary(Salary):
                        print("...Salary in our budget")
                    """if dept_error_check(dep):
                        print("...Department transfer request")
                        else:
                            dep = input("Department not found please enter department again")"""
                    emp = Employee(firstName, lastName, Salary, dep)
                    system.add_New_Employee(emp)
                    print("Employee added")
            elif choice == '2':
                IDupdate = input("Insert Employee ID:\n")
                #ems.update_Employee()
                print("Employee updated")
            elif choice == '3':
                IDremove = input("Enter Employee ID:\n")
                #ems.remove_Employee()
                print("Employee removed")
            elif choice == '4':
                IDlist = input("Enter Employee ID:\n")
                #ems.list_Emp_Info()                
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except:
            InvOption(choice)