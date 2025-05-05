import os
import json
from student import Student

FILE_PATH = 'students.data'

class Database:
    """
    File-based storage for Student records. Supports CRUD operations.
    """
    def __init__(self, path: str = None):
        self.path = path or FILE_PATH
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as f:
                json.dump([], f)

    def _read_all(self) -> list:
        with open(self.path, 'r') as f:
            data = json.load(f)
        return [Student.from_dict(d) for d in data]

    def _write_all(self, students: list):
        with open(self.path, 'w') as f:
            json.dump([s.to_dict() for s in students], f, indent=2)

    def add_student(self, student: Student):
        """Add a new student; error if email exists."""
        all_studs = self._read_all()
        if any(s.email == student.email for s in all_studs):
            raise RuntimeError(f"Student with email {student.email} already exists.")
        all_studs.append(student)
        self._write_all(all_studs)

    def get_student_by_email(self, email: str) -> Student:
        """Retrieve a student by email; error if not found."""
        all_studs = self._read_all()
        for s in all_studs:
            if s.email == email:
                return s
        raise KeyError(f"Student with email {email} not found.")

    def get_student_by_id(self, student_id: str) -> Student:
        for s in self._read_all():
            if s.id == student_id:
                return s
        raise KeyError(f"Student ID {student_id} not found.")

    def update_student(self, student: Student):
        """Replace existing student record by ID."""
        studs = self._read_all()
        updated = False
        for idx, s in enumerate(studs):
            if s.id == student.id:
                studs[idx] = student
                updated = True
                break
        if not updated:
            raise KeyError(f"Student ID {student.id} not found.")
        self._write_all(studs)

    def remove_student_by_id(self, student_id: str):
        studs = self._read_all()
        new = [s for s in studs if s.id != student_id]
        if len(new) == len(studs):
            raise KeyError(f"Student ID {student_id} not found.")
        self._write_all(new)

    def clear_all(self):
        """Remove all student records."""
        self._write_all([])

    def partition_students(self) -> dict:
        """Return dict with 'pass' and 'fail' lists of Student objects."""
        pass_list, fail_list = [], []
        for s in self._read_all():
            (pass_list if s.passed() else fail_list).append(s)
        return {'pass': pass_list, 'fail': fail_list}

    def group_students_by_grade(self) -> dict:
        """Group students by final average grade bucket."""
        groups = {}
        for s in self._read_all():
            avg = round(s.average_mark())
            groups.setdefault(str(avg), []).append(s)
        return groups

    def list_all(self) -> list:
        """Return all Student objects."""
        return self._read_all()
