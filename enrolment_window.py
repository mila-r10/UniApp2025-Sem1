import tkinter as tk
from tkinter import messagebox, Toplevel
from subject import Subject
from database import Database

db = Database()

def open_enrolment_window(student):
    root = tk.Tk()
    root.title("Subject Enrolment")
    root.geometry("400x300")

    subject_frame = tk.Frame(root)
    subject_frame.pack(pady=10)

    def refresh_subject_list():
        for widget in subject_frame.winfo_children():
            widget.destroy()
        tk.Label(subject_frame, text=f"Enrolled Subjects ({len(student.subjects)}/4):").pack()
        for sub in student.subjects:
            tk.Label(subject_frame, text=f"ID: {sub.id}, Mark: {sub.mark}, Grade: {sub.grade}").pack()

    def enrol_subject():
        if len(student.subjects) >= 4:
            messagebox.showwarning("Limit Reached", "You can only enrol in up to 4 subjects.")
            return
        subject = student.enroll()
        db.update_student(student)
        messagebox.showinfo("Enrolled", f"Subject {subject.id} enrolled! Mark: {subject.mark}, Grade: {subject.grade}")
        refresh_subject_list()

    refresh_subject_list()

    tk.Button(root, text="Enrol in Subject", command=enrol_subject).pack(pady=10)
    tk.Button(root, text="View Results", command=lambda: show_results(student)).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()


def show_results(student):
    result_window = Toplevel()
    result_window.title("Subject Results")
    result_window.geometry("400x300")

    if not student.subjects:
        tk.Label(result_window, text="No subjects enrolled.").pack()
        return

    total = 0
    for sub in student.subjects:
        tk.Label(result_window, text=f"ID: {sub.id}, Mark: {sub.mark}, Grade: {sub.grade}").pack()
        total += sub.mark

    avg = total / len(student.subjects)
    status = "PASS" if avg >= 50 else "FAIL"

    tk.Label(result_window, text=f"\nAverage Mark: {avg:.2f}").pack()
    tk.Label(result_window, text=f"Status: {status}").pack()