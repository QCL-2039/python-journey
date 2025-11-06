import os

# ---------- Student Class ----------
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_details(self):
        print(f"Student Name: {self.name} | Student ID: {self.student_id}")

# ---------- File Handling ----------
STUDENT_FILE = "students.txt"

# Load students from file
def load_students():
    students = []
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                name, student_id = line.strip().split(",")
                students.append(Student(name, student_id))
    return students

# Save a new student to file
def save_student(student):
    with open(STUDENT_FILE, "a") as f:
        f.write(f"{student.name},{student.student_id}\n")

# ---------- Main Program ----------
students = load_students()

role = input("Enter your role (admin/student): ").lower()

if role == "admin":
    print("Admin mode: List of all students")
    for stu in students:
        stu.show_details()

elif role == "student":
    action = input("Are you registered already? (yes/no): ").lower()

    if action == "no":
        print("Register new student:")
        name = input("Enter your name: ").strip()
        student_id = input("Enter your ID: ").strip()
        new_student = Student(name, student_id)
        save_student(new_student)
        print("Registration successful!")
        new_student.show_details()

    elif action == "yes":
        student_id = input("Enter your ID to log in: ").strip()
        found = False
        for stu in students:
            if stu.student_id == student_id:
                print("Login successful!")
                stu.show_details()
                found = True
                break
        if not found:
            print("Student not found. Please register first.")

else:
    print("Invalid role!")
