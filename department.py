#Department Class
from employee import Employee

class Department:

    def __init__(self, name, budget, phone):
        self.name = name
        self.budget = budget
        self.phone = phone
        self.emp_count = 0
        
    def set_name(self, name):
        self.name = name
    
    def set_budget(self, budget):
        self.budget = budget
    
    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name
    
    def get_budget(self):
        return self.budget
    
    def get_phone(self):
        return self.phone
    
    def add__emp(self):
        self.emp_count += 1
        return self.emp_count

    def get_emp_count(self):
        return self.emp_count



   