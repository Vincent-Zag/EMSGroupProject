#department_ems
from CSVWriter import CSVWriter

class Dept_ems:
    
    def __init__(self, filepath):
        self.ems_writer = CSVWriter(filepath)
        self.dept = self.ems_writer.read_dept()

    def add_new_department(self, data):
        self.dept.append(data)
        self.ems_writer.write_dept(self.dept)

    def remove_department(self, name):
        before = len(self.dept)
        self.dept =[dept for dept in self.dept if dept.get_name() != name]
        after=len(self.dept)

        if before==0:
            print("No Department in the system currently")

        if before != after:
            print ("Department doesn't exist")

        self.ems_writer.write_dept(self.dept)

    def update_department(self, name, attribute, value):
        self.dept = self.ems_writer.read_dept()
        for department in self.dept:
            if department.get_name() == name:
                att = str(attribute.lower())
                setattr(department, att, value)
                print(department, attribute, value)
                self.ems_writer.write_dept(self.dept)
                return 

        print("You must give a valid Department Name!!")


    def add_employee_to_dept(self, emp):
        #Department.add_to_emp_list(emp)
        pass


    def dept_error_check(self, name):
        self.dept = self.ems_writer.read_dept()
        for Department in self.dept:
            if Department.get_name() == name:
                return False
            else:
                print("Department not Found")
                return True

    def department_info(self, name):
        self.dept = self.ems_writer.read_dept()
        for Department in self.dept:
            if Department.get_name() == name:
                print(f" Department Name: {Department.get_name()} Budget: {Department.get_budget()} Phone: {Department.get_phone()} Employee Count: {Department.get_emp_count()}")
                return
        print("No Department with that name exists")

