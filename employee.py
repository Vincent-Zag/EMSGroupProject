from datetime import date
from datetime import date
import random

class Employee:

    already_use_ids = set()

    def __init__(self, Firstname, Lastname, Salary, Department, employee_id = None, date_of_employement = None):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Salary = Salary
        self.Department = Department
        self.date_of_employment = date_of_employement if date_of_employement else date.today()
        self.employee_id = employee_id if employee_id else self.create_id()
    
    def create_id(self):
        id = random.randint(1, 10000)
        while id in Employee.already_use_ids:
            id = random.randint(1, 10000)
        Employee.already_use_ids.add(id)
        return str(id)

    def get_firstName(self):
        return self.Firstname
    
    def get_lastName(self):
        return self.Lastname
    
    def get_salary(self):
        return self.Salary

    def get_dateOfEmployment(self):
        return self.date_of_employment
    
    def get_employeeId(self):
        return self.employee_id
    
    def get_department(self):
        return self.Department
    
    def set_firstName(self, firstname):
        self.Firstname = firstname
    
    def set_lastName(self, lastname):
        self.Lastname = lastname
    
    def set_salary(self, salary):
        self.Salary = salary
    
    def set_department(self, department):
        self.Department = department