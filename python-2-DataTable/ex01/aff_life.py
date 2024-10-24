import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def main(path: str):
    """
    Plots life expectancy projections for France over the years.

    Args:
        path (str): The file path to the dataset.

    Raises:
        Exception: If an error occurs while loading the data or plotting.
    """
    try:
        ds = load(path)
        data = ds[ds['country'] == 'France']
        years = data.columns[1:]
        life_expectancy = data.values[0][1:]

        plt.figure(figsize=(10, 10))
        plt.plot(np.array(years), np.array(life_expectancy),
                 label="Life Expectancy", color='blue')
        plt.title('France Life Expectancy Projections', fontsize=16)
        plt.xlabel('Year', fontsize=14)
        plt.xticks(years[::40])
        plt.ylabel('Life Expectancy', fontsize=14)
        plt.show()

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("../life_expectancy_years.csv")
