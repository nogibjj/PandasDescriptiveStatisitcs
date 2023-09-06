import pandas as pd


def return_more_than_25th_quantile(df: pd.DataFrame, target: str):
    """ Takes in a dataframe and returns only the top 75th perntile of data
    based on a tatget column (variable) """

    target_quantile = df[target].quantile(0.25)
    df =  df.loc[df[target] > target_quantile]
    
    return df
    

if __name__ == '__main__':
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    target_column = 'sepal_width'

    print(return_more_than_25th_quantile(data, target_column))
