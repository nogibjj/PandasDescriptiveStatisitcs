"""Python Pandas descriptive statistics script"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import ListedColormap, Normalize


def return_25th_quantile(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns 25th quantile of the target column"""

    target_quantile = data_[target].quantile(0.25)

    return target_quantile


def return_mean(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_mean = data_[target].mean()

    return target_mean


def return_std_dev(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the standard deviation of the target column"""

    target_std = data_[target].std()

    return target_std


def return_median(data_: pd.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_median = data_[target].median()

    return target_median


def visualize_dataset(data_: pd.DataFrame, outcome_var: str, target_var: str, inteaction_term: str):
    """Visualizes the passed data"""

    # Get the unique categories from the interaction_term column
    categories = data[inteaction_term].unique()
    # Define a colormap based on the number of unique categories
    cmap = get_cmap("tab10", len(categories))

    # Create a ListedColormap with normalized values
    norm = Normalize(vmin=0, vmax=len(categories) - 1)
    colors = [cmap(norm(i)) for i in range(len(categories))]
    custom_cmap = ListedColormap(colors)

    plt.scatter(
        data_[outcome_var],
        data_[target_var],
        c=data[inteaction_term].apply(lambda x: list(categories).index(x)),
        cmap=custom_cmap)

    plt.xlabel(target_var)
    plt.ylabel(outcome_var)
    plt.title(f"Descriptive Statistivs {target_var} VS {outcome_var}")

    plt.show()
    print(21)


if __name__ == "__main__":
    data = pd.read_csv("data/iris_data.csv")
    TARGET_COLUMN = "sepal_width"

    print(return_25th_quantile(data, TARGET_COLUMN))
    print(return_mean(data, TARGET_COLUMN))
    print(return_median(data, TARGET_COLUMN))
    print(return_std_dev(data, TARGET_COLUMN))

    visualize_dataset(data, "petal_width", TARGET_COLUMN, "species")
