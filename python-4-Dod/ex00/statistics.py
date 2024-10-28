def get_stat(stat: str, data: list):
    """
    Calculates and prints a specified statistical measure of the data.

    Parameters:
        stat (str): The statistic to compute:
        ('mean', 'median', 'quartile', 'std', 'var').
        data (list): The list of numeric data.
    """
    mean = sum(data) / len(data)
    var = sum([(x - mean) ** 2 for x in data]) / len(data)
    if stat == 'mean':
        print(f"mean: {mean}")
    elif stat == 'median':
        data = sorted(data)
        mid = len(data) // 2
        if len(data) % 2 == 0:
            print(f"median: {(data[mid] + data[mid - 1]) / 2}")
        else:
            print(f"median: {data[mid]}")
    elif stat == 'quartile':
        data = sorted(data)
        q1 = data[int(len(data) * 0.25)]
        q2 = data[int(len(data) * 0.75)]
        print(f"quartile: {q1, q2}")
    elif stat == 'std':
        print(f"std: {var ** 0.5}")
    elif stat == 'var':
        print(f"var: {var}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Processes a list of numeric values to compute specified statistics.

    Parameters:
        *args (any): Numeric data points.
        **kwargs (any): Statistical operations requested:
        ('mean', 'median', 'quartile', 'std', 'var').
    """
    if not args:
        print("Error: No data provided.")
        return
    data = [val for val in args if isinstance(val, (int, float))]
    if not data:
        print("Error: No valid values provided.")
        return
    valid_stats = {'mean', 'median', 'quartile', 'std', 'var'}
    req_stats = {value for key, value in kwargs.items()
                 if value in valid_stats}
    if not req_stats:
        print("Error: No valid statistical keys provided.")
        return

    for stat in req_stats:
        get_stat(stat, data)
