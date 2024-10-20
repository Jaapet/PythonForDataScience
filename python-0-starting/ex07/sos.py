import sys

NESTED_MORSE = {' ': '/ ',
                'A': '.- ',
                'B': '-... ',
                'C': '-.-. ',
                'D': '-.. ',
                'E': '. ',
                'F': '..-. ',
                'G': '--. ',
                'H': '.... ',
                'I': '.. ',
                'J': '.--- ',
                'K': '-.- ',
                'L': '.-.. ',
                'M': '-- ',
                'N': '-. ',
                'O': '--- ',
                'P': '.--. ',
                'Q': '--.- ',
                'R': '.-. ',
                'S': '... ',
                'T': '- ',
                'U': '..- ',
                'V': '...- ',
                'W': '.-- ',
                'X': '-..- ',
                'Y': '-.-- ',
                'Z': '--.. ',
                '1': '.---- ',
                '2': '..--- ',
                '3': '...-- ',
                '4': '....- ',
                '5': '..... ',
                '6': '-.... ',
                '7': '--... ',
                '8': '---.. ',
                '9': '----. ',
                '0': '----- '}

table = str.maketrans(NESTED_MORSE)


def main():
    """
    -takes 1 argument, string (alnum and spaces only)
    -if format is wrong, raises AssertionError
    -prints the string converted to morse
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        else:
            str = sys.argv[1]
            if str.replace(" ", "").isalnum():
                print(str.upper().translate(table))
            else:
                raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


if __name__ == "__main__":
    main()
