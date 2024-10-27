class calculator:
    """Calculator class with vector operations."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the dot product of two vectors."""
        res = 0
        for i in V1:
            res += i * V2[V1.index(i)]
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the addition of two vectors."""
        res = []
        for i in V1:
            res.append(i + V2[V1.index(i)])
        print(f"Add vector is: {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints the subtraction of two vectors."""
        res = []
        for i in V1:
            res.append(i - V2[V1.index(i)])
        print(f"Sous vector is: {res}")
