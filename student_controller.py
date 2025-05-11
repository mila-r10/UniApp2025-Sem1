from database import Database
from student import Student
from subject import Subject
import re

db = Database()

def validate_email(email):
    return re.match(r'^[\w\.-]+@university\.com$', email)

def validate_password(password):
    return re.match(r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$', password)

def student_menu():
    while True:
        print("\n=== Student System ===")
        print("(r) Register")
        print("(l) Login")
        print("(x) Exit")

        choice = input("Choose an option: ").lower()

        if choice == 'r':
            register_student()
        elif choice == 'l':
            login_student()
        elif choice == 'x':
            print("Exiting student system.")
            break
        else:
            print("Invalid option.")

def register_student():
    print("\n--- Register ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not validate_email(email):
        print("Invalid email format. Must end with @university.com")
        return

    if not validate_password(password):
        print("Invalid password. Must start with uppercase, have at least 5 letters, and end with 3+ digits.")
        return

    try:
        if db.get_student_by_email(email):
            print("Email already registered.")
            return
    except KeyError:
        pass 

    student = Student(name, email, password)
    db.add_student(student)
    print(f"Registration successful! Your student ID is {student.id}")

def login_student():
    print("\n--- Login ---")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        student = db.get_student_by_email(email)
    except KeyError:
        print("Student not found.")
        return

    if student.password != password:
        print("Incorrect password.")
        return

    print(f"Welcome, {student.name}!")
    subject_enrolment_menu(student)

def subject_enrolment_menu(student):
    while True:
        print(f"\n=== Subject Enrolment for {student.name} ===")
        print("(e) Enrol")
        print("(r) Remove a subject")
        print("(s) Show enrolled subjects")
        print("(c) Change password")
        print("(x) Exit")

        choice = input("Choose: ").lower()

        if choice == 'e':
            if len(student.subjects) >= 4:
                print("You have already enrolled in 4 subjects.")
                continue
            subject = student.enroll() 
            db.update_student(student)
            print(f"Enrolled in subject {subject.id} with mark {subject.mark}, grade {subject.grade}")

        elif choice == 'r':
            sub_id = input("Enter subject ID to remove: ")
            if student.remove_subject(sub_id):
                db.update_student(student)
                print("Subject removed.")
            else:
                print("Subject not found.")

        elif choice == 's':
            if not student.subjects:
                print("No subjects enrolled.")
            for sub in student.subjects:
                print(f"ID: {sub.id}, Mark: {sub.mark}, Grade: {sub.grade}")

        elif choice == 'c':
            new_pass = input("Enter new password: ")
            if validate_password(new_pass):
                student.change_password(new_pass)  
                db.update_student(student)
                print("Password changed.")
            else:
                print("Invalid password format.")

        elif choice == 'x':
            break
        else:
            print("Invalid option.")
