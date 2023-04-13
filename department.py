#Department Class
from CSVWriter import cwrite
from employee import employee

class department:
    def __init__(self, name, budget, phone):
        self.name = name
        self.budget = budget
        self.phone = phone
        self.department_list = []
        self.emp_list = []
        
    def add_department(self, id, emp, name, budget, phone):
        #exception check
        if self.budgetid not in self.department_list:
            self.department_list.append(self.id,self.name,self.budget,self.phone)
        else:
            print("already in list")

    def add_emp_to_department(self, emp):
        if self.id not in self.emp_list:
            print("Department not in selection")
        else:
            self.emp_list.append(self.emp)
    
    def remove_department(self, name):
        if self.id in self.department_list:
            self.department_list.remove(self.name)
        else:
            print("Not in list")
        #find in list then remove the info about department

    def update_department(self, name = None, budget = None, phone = None):
        for name in self.department_list:
            if self.name == name:
                if budget != None:
                    self.budget = budget
                if phone != None: 
                    self.phone = phone
                else: 
                    print("You must enter a valid field to be updated!!!")
            else: 
                print("You must give a valid department Name!!")
        self.ems_writer.write(self.emp)

    def list_department(self):
        with open('employeeData.csv', mode ='r')as file:
            data = cwrite.read(file)
            for lines in data:
                self.department_list.append(lines)
        return self.department_list

    def list_emp_in_department(self):
        with open('employeeDepartment.csv', mode ='r')as file:
            data = cwrite.read(file)
            for lines in data:
                self.emp_list.append(lines)
        return self.emp_list

    def dept_error_check(self, name):
        if self.name not in self.department_list:
            return False
        else:
            return True
