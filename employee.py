from datetime import date
import random

class Employee:

    already_use_ids = set()

    def __init__(self, first_name, last_name, salary, department, employee_id = None, date_of_employement = None):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.date_of_employment = date_of_employement if date_of_employement else date.today()
        self.employee_id = employee_id if employee_id else self.create_id()

    def create_id(self):
        id = random.randomint(1, 10000)
        while id in Employee.already_use_ids:
            id = random.randomint(1, 10000)
        Employee.already_use_ids.add(id)
        return str(id)

    def get_firstName(self):
        return self.first_name
    
    def get_lastName(self):
        return self.last_name
    
    def get_salary(self):
        return self.salary

    def get_dateOfEmployment(self):
        return self.date_of_employment
    
    def get_employeeId(self):
        return self.employee_id
    
    def get_department(self):
        return self.department
