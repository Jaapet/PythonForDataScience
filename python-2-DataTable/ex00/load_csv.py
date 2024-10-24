import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the specified path and return it as a DataFrame.
    Prints its dimensions and the dataset.

    :param path: The path to the CSV file.
    :return: A pandas DataFrame containing the dataset.
    """
    ds = pd.read_csv(path)
    print(f"Loading dataset of dimensions {ds.shape}")
    print(ds)
    return ds
