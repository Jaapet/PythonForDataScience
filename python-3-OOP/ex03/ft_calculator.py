class calculator:
    """Performs arithmetic operations on a vector."""
    def __init__(self, vector) -> None:
        """Initialize with a vector of numbers."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to each element in the vector."""
        self.vector = [val + object for val in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element in the vector by a scalar."""
        self.vector = [val * object for val in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element in the vector."""
        self.vector = [val - object for val in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element in the vector by a scalar,
        handling division by zero."""
        try:
            if object:
                self.vector = [val / object for val in self.vector]
                print(self.vector)
            else:
                raise ZeroDivisionError(" arg cannot be 0")
        except ZeroDivisionError as e:
            print(f"{ZeroDivisionError.__name__}:{e}")
