import sqlite3
import pandas as pd


# Connect Database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# -------------------------------
# Create Students Table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT UNIQUE,
    subject TEXT,
    marks INTEGER
)
""")

# -------------------------------
# Create Attendance Table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

conn.commit()
print("Database and Tables Created Successfully!")

# -------------------------------
# Insert Student
# -------------------------------
def insert_student(name, roll_no, subject, marks):
    try:
        cursor.execute("""
        INSERT INTO students(name, roll_no, subject, marks)
        VALUES (?, ?, ?, ?)
        """, (name, roll_no, subject, marks))

        conn.commit()
        print(f"{name} Inserted Successfully!")

    except sqlite3.IntegrityError:
        print(f"Student with Roll No {roll_no} already exists!")

# -------------------------------
# Update Marks
# -------------------------------
def update_marks(roll_no, new_marks):

    cursor.execute("""
    UPDATE students
    SET marks = ?
    WHERE roll_no = ?
    """, (new_marks, roll_no))

    conn.commit()

    if cursor.rowcount > 0:
        print("Marks Updated Successfully!")
    else:
        print("Student Not Found!")

# -------------------------------
# Delete Student
# -------------------------------
def delete_student(roll_no):

    cursor.execute("""
    DELETE FROM students
    WHERE roll_no = ?
    """, (roll_no,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

# -------------------------------
# Fetch All Students
# -------------------------------
def fetch_students():

    cursor.execute("""
    SELECT *
    FROM students
    ORDER BY marks DESC
    """)

    students = cursor.fetchall()

    print("\n------ Student List ------")

    if not students:
        print("No Students Found!")

    else:
        for student in students:
            print(student)

# -------------------------------
# Students Above 80
# -------------------------------
def students_above_80():

    cursor.execute("""
    SELECT *
    FROM students
    WHERE marks > 80
    ORDER BY marks DESC
    """)

    students = cursor.fetchall()

    print("\n------ Students with Marks > 80 ------")

    if not students:
        print("No Student Found!")

    else:
        for student in students:
            print(student)

# -------------------------------
# Function Calls
# -------------------------------

# Insert Students
insert_student("Ali", "101", "Math", 85)
insert_student("Sara", "102", "Physics", 92)
insert_student("Ahmed", "103", "English", 78)

print("\nInitial Student List")
fetch_students()

# Update Marks
update_marks("103", 88)

print("\nAfter Updating Marks")
fetch_students()

# Delete Student
delete_student("101")

print("\nAfter Deleting Student")
fetch_students()

# Students Above 80
students_above_80()



# -------------------------------
# Average Marks By Subject
# -------------------------------
def average_marks_by_subject():

    cursor.execute("""
    SELECT subject, AVG(marks)
    FROM students
    GROUP BY subject
    """)

    result = cursor.fetchall()

    print("\n------ Average Marks By Subject ------")

    for row in result:
        print(row)


        # -------------------------------
# Add Attendance
# -------------------------------
def add_attendance(student_id, date, status):

    cursor.execute("""
    INSERT INTO attendance(student_id, date, status)
    VALUES (?, ?, ?)
    """, (student_id, date, status))

    conn.commit()

    print("Attendance Added Successfully!")



    # -------------------------------
# Attendance Percentage
# -------------------------------
def attendance_percentage():

    cursor.execute("""
    SELECT
        students.name,

        ROUND(
            100.0 *
            SUM(CASE
                WHEN attendance.status='Present'
                THEN 1
                ELSE 0
            END)
            /
            COUNT(attendance.id),2
        ) AS attendance_percentage

    FROM students

    JOIN attendance
    ON students.id = attendance.student_id

    GROUP BY students.id
    """)

    result = cursor.fetchall()

    print("\n------ Attendance Percentage ------")

    for row in result:
        print(row)



        # -------------------------------
# Top 3 Students
# -------------------------------
def top_three_students():

    cursor.execute("""
    SELECT *
    FROM students
    ORDER BY marks DESC
    LIMIT 3
    """)

    students = cursor.fetchall()

    print("\n------ Top 3 Students ------")

    for student in students:
        print(student)



# Pehle students insert honge:
insert_student("Ali", "101", "Math", 85)
insert_student("Sara", "102", "Physics", 92)
insert_student("Ahmed", "103", "English", 78)


# Phir attendance insert karein:
add_attendance(1, "2026-07-29", "Present")
add_attendance(1, "2026-07-30", "Present")

add_attendance(2, "2026-07-29", "Present")
add_attendance(2, "2026-07-30", "Absent")

add_attendance(3, "2026-07-29", "Present")
add_attendance(3, "2026-07-30", "Present")


# Phir queries call karein:
average_marks_by_subject()
attendance_percentage()
top_three_students()



# generate_report() Function
# Ye function top_three_students() ke baad add karein.
# -------------------------------
# Generate Final Report
# -------------------------------
def generate_report():

    cursor.execute("""
    SELECT
        students.name,
        students.subject,
        students.marks,

        ROUND(
            100.0 *
            SUM(CASE
                WHEN attendance.status = 'Present'
                THEN 1
                ELSE 0
            END)
            /
            COUNT(attendance.id),2
        ) AS attendance_percentage

    FROM students

    JOIN attendance
    ON students.id = attendance.student_id

    GROUP BY students.id
    """)

    report = cursor.fetchall()

    final_report = []

    for row in report:

        name = row[0]
        subject = row[1]
        marks = row[2]
        attendance = row[3]

        if marks > 75 and attendance > 85:
            status = "Eligible"
        else:
            status = "Not Eligible"

        final_report.append(
            [name, subject, marks, attendance, status]
        )

    df = pd.DataFrame(
        final_report,
        columns=[
            "Name",
            "Subject",
            "Marks",
            "Attendance %",
            "Status"
        ]
    )

    print("\n------ Final Report ------")
    print(df)

    df.to_csv("student_report.csv", index=False)

    print("\nCSV File Created Successfully!")

    generate_report()


cursor.close()
conn.close()

print("\nDatabase Connection Closed Successfully!")