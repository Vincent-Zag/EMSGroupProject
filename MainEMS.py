from ems import ems
from employee import Employee
from CSVWriter import CSVWriter

class NameErrorException(Exception):
    pass

class InvalidSalaryError(Exception):
    pass

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

def NameError(name):
    if name.isalpha() == False:
        raise NameErrorException("Name has to have letters only, you cannot have special characters or numbers in your name")
    
    else:
        return True 
    
def InvSalary(salary):
    try:
        salary = int(salary)
    except:
        print("salary has to be int")
    if 30000 < salary < 80000:
        return True
    else:
        raise InvalidSalaryError("Budget between 30000 to 80000") 
    

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
                Salary = input("Enter salary for employee:\n")
                dep = input("Which department?\n")
                
                try:
                    if NameError(firstName):
                        print("...first name is A-Okay")

                    if NameError(lastName):
                        print("...last name ok")
                    
                    if InvSalary(Salary):
                        print("...Salary in our budget")
                    else:
                        break
                        """if dept_error_check(dep):
                            print("...Department transfer request")
                            else:
                                dep = input("Department not found please enter department again")"""

                    emp = Employee(firstName, lastName, Salary, dep)
                    system.add_New_Employee(emp)
                except NameErrorException as e:
                    print(e)
                    print("Employee not added")
                    break
                except InvalidSalaryError as e:
                    print(e)
                    print("employee not added")
                    break

            elif choice == '2':
                update = input("Insert Employee ID:\n")
                updatechar = input("Which attribute do you want to change( Firstname, Lastname, Salary, Department)\n")
                updatechar = updatechar.capitalize()
                if updatechar == 'Firstname' or updatechar == 'Lastname' :
                    try:
                        name = input("Enter name\n")
                        NameError(name)
                        system.update_Employee(update, updatechar, name)
                            
                    except NameErrorException as e:
                        print(e)
                        break
                    
                if updatechar == 'Salary':
                    try:
                        salary = input("Enter Salary change\n")
                        InvSalary(salary)
                        system.update_Employee(update, updatechar, salary)
                    except InvalidSalaryError as e:
                        print(e)
                        break
                if updatechar == 'Department':        
                   pass

            elif choice == '3':
                remove = input("Enter Employee ID:\n")
                system.remove_Employee(remove)
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
