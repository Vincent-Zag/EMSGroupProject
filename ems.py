from fileinput import filename
import employee
from CSVWriter import CSVWriter

class ems:
    #initialize CSV writer 

    def __init__(self, filepath):
        self.ems_writer = CSVWriter(filepath)
        self.emp = self.ems_writer.read(filepath)

    def add_New_Employee(self, employee):
        print("test1")
        self.emp.append(employee)
        self.ems_writer.write(self.emp)
        print("test2")

    def update_Employee(self, e_id, firstname= None, lastname= None, salary= None, department= None):
        for employee in self.emp:
            if employee.employee_id == e_id:
                if firstname != None:
                    employee.firstname = firstname
                if lastname != None: 
                    employee.lastname = lastname
                if salary != None: 
                    employee.salary = salary
                if department != None: 
                    employee.department = department
                else: 
                    print("You must enter a valid field to be updated!!!")
            else: 
                print("You must give a valid employee ID!!")
        self.ems_writer.write(self.emp)
    
        
    #def remove_Employee(self, emp):



    #def list_Emp_Info(self, emp):

