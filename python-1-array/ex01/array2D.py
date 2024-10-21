import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (family) into a smaller 2D list
    based on the given start and end indices.

    Parameters:
    family (list): A 2D list where each sublist must have the same
    length and contain numeric values (int or float).
    start (int): The starting index for slicing (inclusive).
    end (int): The ending index for slicing (exclusive).

    Returns:
    list: A 2D list representing the sliced portion of the input list.
          Returns an empty list if input arguments
          are invalid or if an error occurs.

    Raises:
    AssertionError: If 'family' is not a 2D list or
                    if 'start' and 'end' are not integers.
    """
    try:
        if all(isinstance(e, list) and len(e) == len(family[0]) and
               all(isinstance(el, (int, float))
                   for el in e) for e in family) and\
                    isinstance(family, list) and isinstance(start, int) and\
                    isinstance(end, int):
            arr = np.array(family)
            print(f"My shape is : {arr.shape}")
            print(f"My new shape is : {arr[start:end].shape}")
            return arr[start:end].tolist()
        else:
            raise AssertionError("bad arguments")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        return []
