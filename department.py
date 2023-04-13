#Department Class
from employee import Employee

class Department:
    def __init__(self, name= None, budget = None, phone = None):
        self.name = name
        self.budget = budget
        self.phone = phone
        self.emp_list = []
        
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
    
    def add_to_emp_list(self, emp):
        if self.id not in self.emp_list:
            print("Department not in selection")
        else:
            self.emp_list.append(self.Employee)

    def get_emp_list(self):
        return self.emp_list



   