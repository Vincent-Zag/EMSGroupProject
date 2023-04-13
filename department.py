#Department Class
import CSVWriter

class department():
    def __init__(self, id, name, budget, phone):
        self.id = id
        self.name = name
        self.budget = budget
        self.phone = phone
        self.department_list = []
        
    def add_department(self, id, name, budget, phone):
        self.department_list.append(self.id,self.name,self.budget,self.phone)
    
    def remove_department(self, id):
        #find in list then remove the info about department
        pass

    def update_department(self, attribute_name, new_value):
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
        else:
            print("Invalid attribute")

    def get_list(self):

    def list_depts(self, department_list):

