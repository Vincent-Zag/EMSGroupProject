#department_ems
from fileinput import filename
from CSVWriter import CSVWriter
from employee import Employee
from department import Department

class Dept_ems:

    def __init__(self, filepath):
        self.ems_writer = CSVWriter(filepath)
        self.dept = self.ems_writer.read_dept()

    def add_new_department(self, data):
        self.dept.append(data)
        self.ems_writer.write_dept(self.dept)

    def remove_department(self, name):
        before = len(self.dept)
        self.dept =[dept for dept in self.dept if dept.get_name() != name]
        after=len(self.dept)

        if before==0:
            print("No Department in the system currently")

        if before != after:
            print ("Department doesn't exist")

        self.ems_writer.write_dept(self.dept)

    def update_department(self, name = None, budget = None, phone = None):
        for Department in self.dept:
            if Department.get_name == name:
                if budget != None:
                    Department.budget = budget
                if phone != None: 
                    Department.phone = phone
                else: 
                    print("You must enter a valid field to be updated!!!")
            else: 
                print("You must give a valid department Name!!")
        self.ems_writer.write_dept(self.dept)

    def add_employee_to_dept(self, emp):
        Department.add_to_emp_list(emp)


    def dept_error_check(self, name):
        if self.name not in self.department_list:
            return False
        else:
            return True

    def department_info(self, name):
        self.dept = self.ems_writer.read_dept()
        for Department in self.dept:
            if Department.get_name() == name:
                print(f" Department Name: {Department.get_name()} Budget: {Department.get_budget()} Phone: {Department.get_phone()}")
                return
        print("No Department with that name exists")


def getFileName():
    fileName = input("File Name: ")
    return fileName


def main():
    filename = getFileName()
    system = Dept_ems(filename)

    name = input("Enter name: ")
    budget = input("Enter budget: ")
    phone = input("Enter phone: ")
    dept = Department(name,budget,phone)
    system.add_new_department(dept)

    print(system.department_info('Tech'))
    


main()