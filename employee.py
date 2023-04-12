import time
import random

class Employee:

    already_use_ids = set()

    def __init__(self, first_name, last_name, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.date_of_employment = int(time.time())
        self.employee_id = self.create_id()

    def create_id(self):
        id = random.randomint(1, 10000)
        while id in Employee.already_use_ids:
            id = random.randomint(1, 10000)
        Employee.already_use_ids.add(id)
        return id
