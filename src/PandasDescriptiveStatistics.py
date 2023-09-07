import pandas as pd


def return_25th_quantile(df: pd.DataFrame, target: str) -> float:
    """ Takes in a dataframe and returns 25th quantile of the target column"""

    target_quantile = df[target].quantile(0.25)

    return target_quantile
    

if __name__ == '__main__':
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    target_column = 'sepal_width'

    print(return_25th_quantile(data, target_column))
