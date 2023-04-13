

class ems():

    def __init__(self, emp ):
        self.emp = []
    
    def add_New_Employee(self):
        

    def update_Employee(self, emp):
    

    def remove_Employee(self, id):
        found_employee = None
        for emp in self.emp:
            if emp.id == id:
                found_employee = emp
            break

    # If employee found, remove from list
        if found_employee:
            self.emp.remove(found_employee)
  
    # If employee not found, print error message
        else:
            print("Employee ID not found!!")

    def list_Emp_Info(self, emp):


    