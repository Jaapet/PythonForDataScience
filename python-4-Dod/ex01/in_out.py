def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of x by x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a closure that applies a function to x on each call.

    Parameters:
        x (int | float): Initial value.
        function (callable): Function to apply to x.

        A closure is a function that "remembers" and can access variables
        from its enclosing scope, even after that scope has finished executing.

        The 'nonlocal' keyword allows a nested (inner) function
        to modify a variable in its enclosing (outer) function's scope
        rather than creating a new local variable.
    """
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    return inner
