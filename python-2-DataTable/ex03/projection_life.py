import matplotlib.pyplot as plt
import pandas as pd
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


def main(path1: str, path2: str):
    """
    M
    """
    try:
        income_ds = load(path1)
        life_ds = load(path2)
        income = income_ds[['country', '1900']]
        life = life_ds[['country', '1900']]

        #  rename columns
        income.columns = ['country', 'income']
        life.columns = ['country', 'life']

        merge = pd.merge(life, income, on='country').dropna()

        income = merge['income']
        life = merge['life']

        plt.figure(figsize=(10, 10))
        plt.scatter(income, life, color='blue', label="1900")
        plt.title('1900', fontsize=16)
        plt.xlabel('Gross Domestic Product', fontsize=14)
        plt.ylabel('Life Expectancy', fontsize=14)

        plt.show()

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
         "../life_expectancy_years.csv")
