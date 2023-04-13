from CSVWriter import CSVWriter

class ems:

    def __init__(self, filepath):
        self.ems_writer = CSVWriter(filepath)
        self.emp = self.ems_writer.read()

    def add_New_Employee(self, employee):
        self.emp.append(employee)
        self.ems_writer.write(self.emp)

    def update_Employee(self, e_id, firstname= None, lastname= None, salary= None, department= None):
        self.emp = self.ems_writer.read()
        for employee in self.emp:
            if employee.get_employeeId() == e_id:
                if firstname != None:
                    employee.set_firstName(firstname)
                if lastname != None: 
                    employee.set_lastName(lastname)
                if salary != None: 
                    employee.set_salary(salary)
                if department != None: 
                    employee.set_department(department)
                self.ems_writer.write(self.emp)
                print("Employee updated")
                break
            else: 
                print("You must give a valid employee ID!!")
    

    def remove_Employee(self, id):
        self.emp=self.ems_writer.read()
        before=len(self.emp)
        self.emp=[emp for emp in self.emp if emp.get_employeeId() != id]
        after=len(self.emp)
        if before==0:
            print("No employee in the system currently")
        if before != after:
            print ("employee ID doesn't exist")
        self.ems_writer.write(self.emp)

    def list_Emp_Info(self, id):
        self.emp = self.ems_writer.read()
        for employee in self.emp:
            if employee.get_employeeId() == id:
                print(f" ID: {employee.get_employeeId()} Name: {employee.get_firstName()} {employee.get_lastName()}, Salary: {employee.get_salary()}, Date of Employement: {employee.get_dateOfEmployment()}, Department: {employee.get_department()}")
                return
        print("No employee exists with that ID")

