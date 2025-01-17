import csv
import logging

logging.basicConfig(filename='student_record.log', level=logging.DEBUG,
                    format='%(asctime)s , %(levelname)s , %(message)s')


class studentScore:
    def __init__(self, csv_file='student_data.csv'):
        self.csv_file = csv_file

    def RetrieveStudentScore(self, Rollno):
        """
        Retrieves the student score based on the given Rollno.

        Parameters:
        Rollno (int): The roll number of the student.

        Returns:
        dict: A dictionary containing the student's details if found.
        """
        try:
            with open(self.csv_file, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['Rollno'] == str(Rollno):
                        logging.info(f"Record found for rollno {Rollno}")
                        return row
                logging.warning(f"No records found for rollno {Rollno}")
                print(f"No records found for rollno {Rollno}")
        except Exception as e:
            logging.error(f"Error retrieving student score: {e}")
            print(f"Error retrieving student score: {e}")

    def StoreStudentScore(self):
        """
        Stores the student score by collecting input from the user.

        Prompts the user to enter student details and saves them to the CSV file.
        """
        data = {}
        data['Rollno'] = input("Enter RollNo: ").strip()
        data['name'] = input("Enter student name: ").strip()
        data['english'] = input("Enter English score: ").strip()
        data['maths'] = input("Enter Maths score: ").strip()
        data['science'] = input("Enter Science score: ").strip()

        missing = [key for key, value in data.items() if not value]
        if missing:
            logging.error(f"Failed to store data, following parameters missing: {', '.join(missing)}")
            print(f"Failed to store data, following parameters missing: {', '.join(missing)}")
            return

        try:
            with open(self.csv_file, mode='a', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=data.keys())
                # print(csv_writer)
                csv_writer.writerow(data)
                logging.info("Student data stored successfully")
                print("Student data stored successfully")
        except Exception as e:
            logging.error(f"Error storing student score: {e}")
            print(f"Error storing student score: {e}")

    def mainMenu(self):
        """
        Displays the main menu and prompts the user to choose an option.

        Options:
        1. Retrieve Student Score
        2. Store Student Score
        3. Calculate Average Scores
        4. Display All Records
        5. Exit
        """
        while True:
            print("Main Menu")
            print("1. Retrieve Student Score")
            print("2. Store Student Score")
            print("3. Calculate Average Scores")
            print("4. Display All Records")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                rollno = int(input("Enter RollNo: ").strip())
                print(self.RetrieveStudentScore(rollno))
            elif choice == '2':
                self.StoreStudentScore()
            elif choice == '3':
                self.calculateAverage()
            elif choice == '4':
                header = input("Enter the header to sort by: ").strip()
                sort_order = input("Enter sort order (asc/desc): ").strip().lower() == 'asc'
                self.displayAll(header, sort_order)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def calculateAverage(self):
        """
        Calculates the average score of 3 subjects per student and updates the CSV file.
        """
        try:
            with open(self.csv_file, mode='r') as file:
                csv_reader = csv.DictReader(file)
                students = list(csv_reader)

            for student in students:
                student['average'] = (int(student['english']) + int(student['maths']) + int(student['science'])) // 3

            with open(self.csv_file, mode='w', newline='') as file:
                fieldnames = students[0].keys()
                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(students)

            logging.info("Average scores calculated and CSV updated successfully")
            print("Average scores calculated and CSV updated successfully")
        except Exception as e:
            logging.error(f"Error calculating average scores: {e}")
            print(f"Error calculating average scores: {e}")


    def displayAll(self, header, sort_order=True):
        """
        Displays all the records sorted by the specified header and order.

        Parameters:
        header (str): The column name to sort by.
        sort_order (bool): True for ascending, False for descending.
        """
        try:
            with open(self.csv_file, mode='r') as file:
                csv_reader = csv.DictReader(file)
                records = list(csv_reader)
            print(records[0])

            if header not in records[0]:
                logging.error(f"Header not found: {header}")
                print(f"Header not found: {header}")
                return

            records.sort(key=lambda x: x[header], reverse=not sort_order)

            for record in records:
                print(record)

            logging.info(f"Records displayed sorted by {header} in {'ascending' if sort_order else 'descending'} order")
        except Exception as e:
            logging.error(f"Error displaying records: {e}")
            print(f"Error displaying records: {e}")


s = studentScore('student_data.csv')
s.mainMenu()