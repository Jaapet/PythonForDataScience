import sys
import string


def count(str):
    """
    str (input string): The text to analyze

    Prints the following information:
    1. The number of characters in str
    2. The number of upper case letters
    3. The number of lower case letters
    4. The number of punctuation marks
    5. The number of spaces
    6. The number of digits
    """
    print(f"The text contains {len(str)} characters:")
    print(f"{sum(1 for char in str if char.isupper())} lower letters")
    print(f"{sum(1 for char in str if char.islower())} upper letters")
    print(f"{sum(1 for char in str if char in string.punctuation)} \
        punctuation marks")
    print(f"{sum(1 for char in str if char.isspace())} spaces")
    print(f"{sum(1 for char in str if char.isdigit())} digits")


def main():
    """
    Analyzes the given text and prints information about its content.

    Asks for input if no argument is given,
    raises AssertionError: Too many arguments provided if more than 1 argument.
    """
    try:
        if len(sys.argv) < 2:
            try:
                str = input("What is the text to count?\n")
                str += '\n'
            except EOFError:
                pass
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            str = sys.argv[1]
        count(str)
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


if __name__ == "__main__":
    main()
