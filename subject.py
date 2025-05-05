import random
from uuid import uuid4

class Subject:
    """
    Subject 的属性为: id, mark, grade
    """

    def __init__(self, id: str = None, mark: int = None):
        # 3-digit unique ID
        self.id = id or f"{uuid4().int % 1000:03d}"
        self.mark = mark if mark is not None else random.randint(1, 100)
        self.grade = self._calc_grade(self.mark)

    @staticmethod
    def _calc_grade(mark: int) -> str:
        # Example grading scale
        if mark >= 85:
            return 'HD'  # High Distinction
        elif mark >= 75:
            return 'D'   # Distinction
        elif mark >= 65:
            return 'C'   # Credit
        elif mark >= 50:
            return 'P'   # Pass
        else:
            return 'F'   # Fail

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Subject':
        return cls(id=data['id'], mark=data['mark'])