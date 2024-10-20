import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
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
