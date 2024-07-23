import csv

class studentScore:
    def __init__(self, csv_file='student_data.csv'):
        self.csv_file = csv_file

    def RetrieveStudentScore(self, Rollno):
        with open(self.csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['Rollno'] == str(Rollno):
                    return {
                        "Rollno": row['Rollno'],
                        "name": row['name'],
                        "english": row['english'],
                        "maths": row['maths'],
                        "science": row['science']
                    }
            return f"No records found for rollno {Rollno}"