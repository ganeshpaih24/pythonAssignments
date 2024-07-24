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

    def StoreStudentScore(self):
        data = {}
        data['Rollno'] = input("Enter RollNo: ").strip()
        data['name'] = input("Enter student name: ").strip()
        data['english'] = input("Enter English score: ").strip()
        data['maths'] = input("Enter Maths score: ").strip()
        data['science'] = input("Enter Science score: ").strip()

        missing = [key for key, value in data.items() if not value]
        if missing:
            print(f"Failed to store data, following parameters missing: {', '.join(missing)}")
            return

        with open(self.csv_file, mode='a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=data.keys())
            csv_writer.writerow(data)
            print("Student data stored successfully")

    def mainMenu(self):
        while True:
            print("Main Menu")
            print("1. Retrieve Student Score")
            print("2. Store Student Score")
            print("2. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                rollno = int(input("Enter RollNo: ").strip())
                print(self.RetrieveStudentScore(rollno))
            elif choice == '2':
                self.StoreStudentScore()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")