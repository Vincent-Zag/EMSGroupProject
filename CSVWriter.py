import csv

#Writer class for reading and writing to csv

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        
    def write(self, data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    
    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                return rows
        except:
            print("No such file exists")
        

        
#To initialize please use        
#writer = CSVWriter('EmployeeData.csv')
#writer.read('EmployeeData.csv')

