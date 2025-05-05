import re
from uuid import uuid4
from subject import Subject

EMAIL_REGEX = r'^[\w\.]+@university\.com$'
PASSWORD_REGEX = r'^[A-Z][A-Za-z]{4,}\d{3,}$'

class Student:
    """
    student: id, name, email, password and enrolled subjects.
    -> enrollment, removal, password change, and serialization.
    """
    def __init__(self, name: str, email: str, password: str, id: str = None, subjects=None):
        # Validate email and password on creation
        if not re.match(EMAIL_REGEX, email):
            raise ValueError(f"Invalid email format: {email}")
        if not re.match(PASSWORD_REGEX, password):
            raise ValueError("Password must start with uppercase, have at least 5 letters, then 3+ digits.")

        self.id = id or self._generate_id()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects or []  

    @staticmethod
    def _generate_id() -> str:
        # ID: 6-digit unique numbers
        return f"{uuid4().int % 1_000_000:06d}"


    def enroll(self) -> Subject:
        """Enroll in a new subject if fewer than 4 enrolled."""
        if len(self.subjects) >= 4:
            raise RuntimeError("No more than 4 subjects for enrollment.")
        subj = Subject()
        self.subjects.append(subj)
        return subj

    def remove_subject(self, subject_id: str):
        # Remove an enrolled subject by its ID.
        before = len(self.subjects)
        self.subjects = [s for s in self.subjects if s.id != subject_id]
        if len(self.subjects) == before:
            raise KeyError(f"Subject {subject_id} not found.")

    def change_password(self, new_password: str):

        if not re.match(PASSWORD_REGEX, new_password):
            raise ValueError("Password must start with uppercase, have at least 5 letters, then 3+ digits.")
        self.password = new_password

    def average_mark(self) -> float:

        if not self.subjects:
            return 0.0
        return sum(s.mark for s in self.subjects) / len(self.subjects)

    def passed(self) -> bool:

        return self.average_mark() >= 50

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': [s.to_dict() for s in self.subjects]
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        subs = [Subject.from_dict(sd) for sd in data.get('subjects', [])]
        return cls(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            id=data['id'],
            subjects=subs
        )