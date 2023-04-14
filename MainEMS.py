from ems import ems
from employee import Employee
from department import Department
from department_ems import Dept_ems
from CSVWriter import CSVWriter

class NameErrorException(Exception):
    pass

class InvalidSalaryError(Exception):
    pass

class InvalidInputError(Exception):
    pass

def getFileName(inpt):
    if int(inpt) == 1:
        fileName = input("Enter CSV file name for Employees: ")
    elif int(inpt) == 2:
        fileName = input("Enter CSV file name for Departments: ")
    if fileName[-4:] != '.csv':
        fileName += '.csv'
    return fileName

def main_menu():
    print("==============================")
    print("1. Add Employee")
    print("2. Update existing Employee")
    print("3. Remove Employee")
    print("4. List current Employee")
    print("5. Department Menu")
    print("6. Exit")
    print("==============================")
    choice = input("Enter your choice: ")
    print()
    return choice

def main_menu_department():
    print("==============================")
    print("1. Add Department")
    print("2. Update existing Department")
    print("3. Remove Department")
    print("4. List current Departments")
    print("5. Exit")
    print("==============================")
    choice = input("Enter your choice: ")
    print()
    return choice

def NameError(name):
    if name.isalpha() == False:
        raise NameErrorException("Name has to have letters only, you cannot have special characters or numbers in your name")
    else:
        return True 
    
def InputError(value):
    try:
        value = int(value)
    except:
        print("Input has to be an Int Value")
        raise InvalidInputError("Invalid Input, only Int values allowed")

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
    if option > 6 or option < 1:
        print("invalid option")


def emp_menu():
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

                    if not dept_system.dept_error_check(dep):
                        print("...Department Exists")
                    else:  
                        break
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
                update = input("Insert Employee ID: ")
                updatechar = input("Which attribute do you want to change(Firstname, Lastname, Salary, Department): ")
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
                    print("That is not implemented yet. SoonTM")
                    pass

            elif choice == '3':
                remove = input("Enter Employee ID:\n")
                system.remove_Employee(remove)
            elif choice == '4':
                display = input("Enter Employee ID:\n")
                system.list_Emp_Info(display)
            elif choice == '5':
                print("Switching to Department Menu.")
                break
            elif choice == '6':
                print("Exiting Menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except:
            InvOption(choice)


def dept_menu():
    while True:
        choice = main_menu_department()
        try:
            if choice == '1':
                    name = input("Enter Department Name: ")
                    budget = input("Enter Department Budget: ")
                    p_num = input("Enter Phone Number: ")
                    
                    try:
                        if NameError(name):
                            print("...first name is A-Okay")
                        if InvalidInputError(budget):
                            print("...budget inputted")
                        else:  
                            break

                        department = Department(name,budget,p_num)
                        dept_system.add_new_department(department)

                    except NameErrorException as e:
                        print(e)
                        print("Department Name not Added")
                        break
                    except InvalidInputError as e:
                        print(e)
                        print("Invalid Input")
                        break
            elif choice == '2':
                    name = input("Enter Department name you want to Update: ")
                    updateVal = input("Which attribute do you want to change (Budget, Phone): ")
                    updateVal = updateVal.capitalize()
                    if updateVal == 'Budget':
                        try:
                            budget = input("Enter Budget value: ")
                            NameError(name)
                            dept_system.update_department(name,updateVal,budget)
                        except NameErrorException as e:
                            print(e)
                            print("Department Name not Added")
                            break 
                    if updateVal == 'Phone':
                        try:
                            p_num = input("Enter Phone Number: ")
                            InvalidInputError(p_num)
                            dept_system.update_department(name,updateVal,p_num)

                        except InvalidInputError as e:
                            print(e)
                            print("Invalid Input")
                            break
                    
            elif choice == '3':
                remove = input("Enter Department Name: ")
                dept_system.remove_department(remove)
            elif choice == '4':
                display = input("Enter Department Name: ")
                dept_system.department_info(display)
            elif choice == '5':
                print("Goodbye!")
                break
        except:
            InvOption(choice)


if __name__=='__main__':
    filename = getFileName(1)
    system = ems(filename)
    dept_filename = getFileName(2)
    dept_system = Dept_ems(dept_filename)

    while True:
        emp_menu()
        dept_menu()
        ans = input("Go back to Employee menu? y or n: ")
        if ans == 'y':
            continue
        else:
            break
