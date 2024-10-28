def callLimit(limit: int):
    """
    A decorator to limit the number of times
    a function can be called.

    Parameters:
        limit (int): The maximum number of
        allowed calls for the decorated function.

    Returns:
        function: A wrapped function that raises an
        error message after exceeding the call limit.
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
