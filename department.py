#Department Class
import CSVWriter as cwrite
import employee

class department():
    def __init__(self, name, budget, phone):
        self.name = name
        self.budget = budget
        self.phone = phone
        self.department_list = []
        self.dept_emp_list = {}
        
    def add_department(self, id, emp, name, budget, phone):
        #exception check
        if id not in self.department_list:
            self.department_list.append(self.id,self.name,self.budget,self.phone)
        else:
            print("already in list")

    def add_emp_to_department(self, id, emp):
        if id not in self.department_list:
            print("Department not in selection")
        else:
            data = {i for i in dept_emp_list if dict_1[i]=="id"}
    
    def remove_department(self, id):
        if id in self.department_list:
            pass
        else:
            print("Not in list")
        #find in list then remove the info about department

    def update_department(self, attribute_name, new_value):
        if hasattr(self, attribute_name):
            setattr(self, attribute_name, new_value)
        else:
            print("Invalid attribute")

    def list_department(self):
        with open('employeeData.csv', mode ='r')as file:
            data = cwrite.read(file)
            for lines in data:
                self.department_list.append(lines)
        return self.department_list

    def list_emp_department(self):
        with open('employeeDepartment.csv', mode ='r')as file:
            data = cwrite.read(file)
            for key, value in data:
                self.dept_emp_list.append(key,value)
        return self.dept_emp_list

    def dept_error_check(self, name):
        if name not in self.department_list:
            return False
        else:
            return True
