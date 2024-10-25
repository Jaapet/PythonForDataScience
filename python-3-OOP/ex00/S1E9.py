from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character with a name and life status."""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character with a name and life status.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): Life status, default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mark the character as deceased."""
        pass


class Stark(Character):
    """Represents a Stark family member with life status management."""
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Stark family member with a name and life status.

        Args:
            first_name (str): The Stark member's first name.
            is_alive (bool): Life status, default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's life status to deceased."""
        self.is_alive = False
