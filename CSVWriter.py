import csv

#Writer class for inseting, deleting and updating CSV file 

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        
    def write(self, data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    
    def delete(filename, column_index, value):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row[column_index] != value:
                    writer.writerow(row)

    def update(filename, ):
        
csvwriter = CSVWriter('EmployeeData.csv')
csv_writer.write(['habib', 'mulla', 50000, 'data analyst'])
