from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represents a King with life status management."""
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a King with a name and life status.

        Args:
            first_name (str): The Baratheon member's first name.
            is_alive (bool): Life status, default is True.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """
        Getter for eyes value.
        """
        return self.eyes

    def get_hairs(self):
        """
        Getter for hairs value.
        """
        return self.hairs

    def set_eyes(self, val):
        """
        Setter for eyes value.
        """
        self.eyes = val

    def set_hairs(self, val):
        """
        Setter for eyes value.
        """
        self.hairs = val
