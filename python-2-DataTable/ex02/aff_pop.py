import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def n_pop(pop: str) -> float:
    """
    Convert population string to float.

    Args:
        pop (str): Population value as a string,
        potentially suffixed with 'M' (millions) or 'k' (thousands).

    Returns:
        float: Population as a float.
    """
    if pop.endswith("M"):
        return float(pop[:-1]) * 1e6
    elif pop.endswith("k"):
        return float(pop[:-1]) * 1e3
    else:
        return float(pop)


def main(path: str):
    """
    Main function to plot population projections for France and Belgium.

    Args:
        path (str): Path to the CSV file containing population data.

    Raises:
        Exception: If data loading or processing encounters an error.
    """
    try:
        ds = load(path)
        data_f = ds[ds['country'] == 'France']
        years = data_f.columns[1:].astype(int)
        pop_f = [n_pop(val) for val in data_f.values[0][1:]]

        data_b = ds[ds['country'] == 'Belgium']
        pop_b = [n_pop(val) for val in data_b.values[0][1:]]

        years_range = np.arange(1800, 2051)
        pop_f = np.interp(years_range, years, pop_f)
        pop_b = np.interp(years_range, years, pop_b)

        pop_max = max(max(pop_f), max(pop_b))

        plt.figure(figsize=(10, 10))

        plt.plot(years_range, pop_b,
                 label="Belgium", color='blue')
        plt.plot(years_range, pop_f,
                 label="France", color='green')

        plt.title('Population Projections', fontsize=16)

        plt.xlabel('Year', fontsize=14)
        plt.xticks(years_range[::40])
        yticks = [i * 1e7 for i in range(int(pop_max / 1e7) + 1)]

        plt.ylabel('Population', fontsize=14)
        plt.yticks(yticks, ["{:,.0f}M".format(n_pop / 1e6)
                            for n_pop in yticks])

        plt.legend(loc='lower right')
        plt.show()

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("../population_total.csv")
