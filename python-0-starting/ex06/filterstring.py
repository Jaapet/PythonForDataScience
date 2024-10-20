import sys


def filterstring(fun, str):

    """
    filterstring(function, string) --> list

    This is a custom implementation of the built-in filter function.
    It returns an iterator that yields only the words in 'str'
    for which 'fun' returns 'True'.
    """

    return [word for word in str if fun(word)]


def main():
    """
    -takes 2 arguments, string (alnum and spaces only) and int
    -if format is wrong, raises AssertionError
    -prints the words that are greater or equal in length than the int
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        else:
            args = sys.argv[1:]
            if isinstance(args[0], str) and args[0].replace(" ", "").isalnum():
                try:
                    print(filterstring(lambda word: len(word) >= int(args[1]),
                                       args[0].split()))
                except ValueError:
                    raise AssertionError("the arguments are bad")
            else:
                raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


if __name__ == "__main__":
    main()
