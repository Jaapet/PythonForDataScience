import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character string ID with lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student with a unique ID, name, surname, and login.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's surname.
        active (bool): The student's status, active by default.
        student_id (str): Auto-generated unique ID.
        login (str): Login name generated after initialization.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    student_id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)  # Exclude from __init__, callable above

    def __post_init__(self):
        """Generates the login attribute after
        initialization based on name and surname."""
        self.login = f"{self.name[0].upper() + self.surname.lower()}"
