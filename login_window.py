import tkinter as tk
from tkinter import messagebox
from database import Database
from enrolment_window import open_enrolment_window

db = Database()

def attempt_login():
    email = email_entry.get()
    password = password_entry.get()

    try:
        student = db.get_student_by_email(email)
        if student.password == password:
            print("✅ Login successful.")
            root.destroy()
            open_enrolment_window(student)
        else:
            print("❌ Incorrect password.")
            messagebox.showerror("Error", "Incorrect password.")
    except KeyError:
        print("❌ Student not found.")
        messagebox.showerror("Error", "No such student. Please register first.")

root = tk.Tk()
root.title("Student Login")
root.geometry("350x200")

# ==== 加粗字体 ====
tk.Label(root, text="Email:", font=("Arial", 12, "bold")).pack(pady=(15, 5))
email_entry = tk.Entry(root, width=30, font=("Arial", 12, "bold"))
email_entry.pack()

tk.Label(root, text="Password:", font=("Arial", 12, "bold")).pack(pady=(15, 5))
password_entry = tk.Entry(root, width=30, show="*", font=("Arial", 12, "bold"))
password_entry.pack()

tk.Button(root, text="Login", font=("Arial", 12, "bold"), command=attempt_login).pack(pady=20)

root.mainloop()
