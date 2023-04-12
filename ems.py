

class ems():

    def __init__(self):
        self.emp = []
    
    def add_New_Employee(self, employee):
        for employee in self.emp: 
            if employee in self:
                print("This employee ID already exist, enter a valid ID: ")
            else: 
                self.emp.append(employee)

    def update_Employee(self, attribute_name, new_value):
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
        else:
            print("Invalid attribute")

    write_employee_list = csvwriter.write(self.emp)
        
    def remove_Employee(self, emp):


    def list_Emp_Info(self, emp):


    