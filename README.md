# Student-Management-System
# Student Database System

## Project Overview

The Student Database System is a Python-based application that manages student records using SQLite. It provides features for storing student information, managing attendance, performing data analysis, and generating reports using Pandas.

---

## Technologies Used

- Python
- SQLite3
- Pandas

---

## Database

The project uses an SQLite database named:

```
school.db
```

### Database Tables

### Students Table

| Column | Description |
|--------|-------------|
| id | Student ID (Primary Key) |
| name | Student Name |
| roll_no | Unique Roll Number |
| subject | Subject Name |
| marks | Student Marks |

### Attendance Table

| Column | Description |
|--------|-------------|
| id | Attendance ID |
| student_id | Student ID (Foreign Key) |
| date | Attendance Date |
| status | Present / Absent |

---

## Features

### Student Management

- Insert new student records
- Update student marks
- Delete student records
- Display all students
- Display students with marks greater than 80
- Display students ordered by marks

---

### Attendance Management

- Add attendance records
- Store attendance status (Present/Absent)
- Calculate attendance percentage for each student

---

### Data Analysis

- Calculate average marks by subject
- Display Top 3 students based on marks
- Generate attendance percentage report

---

### Final Report Generation

Generate a report containing:

- Student Name
- Subject
- Marks
- Attendance Percentage
- Eligibility Status

Eligibility Criteria:

- Marks > 75
- Attendance > 85%

---

### Export Report

The final report is exported as:

```
student_report.csv
```

---

## Project Structure

```
Student-Database-System/
│
├── student_database_system.py
├── school.db
├── student_report.csv
└── README.md
```

---

## Required Libraries

Install the required library:

```bash
pip install pandas
```

---

## How to Run

Run the project using:

```bash
python student_database_system.py
```

---

## Output

The system performs the following tasks:

- Creates SQLite database and tables
- Inserts student records
- Updates student marks
- Deletes student records
- Displays student information
- Manages attendance records
- Calculates attendance percentage
- Calculates average marks by subject
- Displays top 3 students
- Generates final student report
- Exports the report to CSV

---

## Learning Outcomes

Through this project, I learned:

- SQLite Database Management
- CRUD Operations (Create, Read, Update, Delete)
- SQL Queries
- Aggregate Functions
- JOIN Operations
- Foreign Keys
- Pandas DataFrame
- CSV File Export
- Report Generation

---

## Author

**Ahmad Raza**
