from S1E9 import Character


class Baratheon(Character):
    """Represents a Baratheon family member with life status management."""
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Baratheon family member with a name and life status.

        Args:
            first_name (str): The Baratheon member's first name.
            is_alive (bool): Life status, default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set the character's life status to deceased."""
        super().die()

    def __str__(self):
        # Return a user-friendly string
        return f"Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

    def __repr__(self):
        # Return an unambiguous string that represents the object
        return self.__str__()


class Lannister(Character):
    """Represents a Lannister family member with life status management."""
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Lannister family member with a name and life status.

        Args:
            first_name (str): The Lannister member's first name.
            is_alive (bool): Life status, default is True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set the character's life status to deceased."""
        super().die()

    def __str__(self):
        # Return a user-friendly string
        return f"Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

    def __repr__(self):
        # Return an unambiguous string that represents the object
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Create a Lannister character instance with custom is_alive status.

        Args:
            first_name (str): The member's first name.
            is_alive (bool): Life status.

        Returns:
            Lannister: An instance of the Lannister character.
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
