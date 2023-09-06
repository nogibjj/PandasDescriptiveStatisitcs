from src.PandasDescriptiveStatistics import return_more_than_25th_quantile
import pandas as pd


def test_return_more_than_25th_quantile():
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    target_column = 'sepal_width'

    res =  return_more_than_25th_quantile(data, target_column)
    
    target_quantile = df[target_column].quantile(0.25)
    data =  data.loc[data[target] > target_quantile]
    
    assert data == res
