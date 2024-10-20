import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    """
    Calculate the BMI for each height and weight pair.

    Args:
        height (list[int | float]): List of heights (must be positive numbers).
        weight (list[int | float]): List of weights (must be positive numbers).

    Returns:
        list[int | float]: List of BMI values, or an empty list on error.
    """

    try:
        if len(height) == len(weight) and\
            all(isinstance(h, (int, float)) and h > 0 for h in height) and\
                all(isinstance(w, (int, float)) and w > 0 for w in weight):
            arr1 = np.array(height)
            arr2 = np.array(weight)
            return list(arr2 / (arr1 * arr1))
        else:
            raise AssertionError("bad arguments")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    """
    Check if BMI values exceed a given limit.

    Args:
       bmi (list[int | float]): List of BMI values (must be positive numbers).
       limit (int): Threshold limit (must be a positive integer).

    Returns:
       list[bool]: List of boolean values indicating whether
       each BMI exceeds the limit, or an empty list on error.
    """

    try:
        if all(isinstance(x, (int, float)) and x > 0 for x in bmi) and\
                isinstance(limit, int) and limit > 0:
            return list(element > limit for element in bmi)
        else:
            raise AssertionError("bad arguments")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
        return []
