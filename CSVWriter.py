import csv
from employee import Employee
from department import Department
#Writer class for reading and writing to csv

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        
    def write(self, data):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee Id", "First Name", "Last Name", "Salary", "Department", "Date of Employment"])
            for employee in data:
                writer.writerow([employee.get_employeeId(), employee.get_firstName(), employee.get_lastName(), employee.get_salary(), employee.get_department(), employee.get_dateOfEmployment()])
            print("Employees added to CSV file")
    
    def write_dept(self, data):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Department Name", "Budget", "Phone Number"])
            for department in data:
                writer.writerow([department.get_name(), department.get_budget(), department.get_phone()])
            print("Department added to CSV file")
    

    def read(self):
        try:
            employees = []
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    employee = Employee(row[1], row[2], row[3], row[4], row[0], row[5])
                    employees.append(employee)
            return employees
        except FileNotFoundError:
            print("No such file exists")
            return []
    
    def read_dept(self):
        try:
            depts = []
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    dept = Department(row[0], row[1], row[2])
                    depts.append(dept)
            return depts
        except FileNotFoundError:
            print("No such file exists")
            return []