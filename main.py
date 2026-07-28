import json

# Student Class

class Student:

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    # Add Subject Marks
    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    # Calculate Average
    def get_average(self):

        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    # Get Grade
    def get_grade(self):

        average = self.get_average()

        if average >= 90:
            return "A"

        elif average >= 80:
            return "B"

        elif average >= 70:
            return "C"

        else:
            return "F"

    # Display Student
    
    def display(self):

        print("STUDNT RECORDD")
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Marks     :", self.marks)
        print("Average   :", round(self.get_average(), 2))
        print("Grade     :", self.get_grade())


# Scholarship Student


class ScholarshipStudent(Student):

    def check_scholarship(self):

        if self.get_average() > 85:
            return "Eligible for Scholarship"

        else:
            return "Not Eligible for Scholarship"


# School Class


class School:

    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self, student):
        self.students.append(student)

    # Show All Students
    def show_all_students(self):

        print("\n========== STUDENT LIST ==========")

        for student in self.students:
            student.display()

    # Find Topper
    def topper(self):

        if len(self.students) == 0:
            return None

        top = self.students[0]

        for student in self.students:

            if student.get_average() > top.get_average():
                top = student

        return top

    
    # Save to JSON
  

    def save_to_json(self, filename):

        data = []

        for student in self.students:

            student_data = {

                "name": student.name,
                "roll_no": student.roll_no,
                "marks": student.marks

            }

            data.append(student_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("\nData Saved Successfully!")

    # Load from JSON
    

    def load_from_json(self, filename):

        try:

            with open(filename, "r") as file:

                data = json.load(file)

            self.students = []

            for item in data:

                student = Student(item["name"], item["roll_no"])
                student.marks = item["marks"]

                self.students.append(student)

            print("\nData Loaded Successfully!")

        except FileNotFoundError:

            print("\nFile Not Found!")



# Testing


student1 = Student("Ali", 101)
student1.add_marks("Math", 90)
student1.add_marks("English", 85)
student1.add_marks("Science", 88)

student2 = Student("Sara", 102)
student2.add_marks("Math", 98)
student2.add_marks("English", 95)
student2.add_marks("Science", 92)

student3 = ScholarshipStudent("Ahmed", 103)
student3.add_marks("Math", 90)
student3.add_marks("English", 88)
student3.add_marks("Science", 87)

# Scholarship
print("\nScholarship Status:")
print(student3.check_scholarship())

# School Object


school = School()

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.show_all_students()


# Topper


top = school.topper()

print("\n========== TOPPER ==========")

top.display()


# Save JSON


school.save_to_json("students.json")

# Load JSON


new_school = School()

new_school.load_from_json("students.json")

print("\n========== DATA FROM JSON ==========")

new_school.show_all_students()



        