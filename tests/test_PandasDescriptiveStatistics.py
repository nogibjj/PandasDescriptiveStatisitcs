from src.PandasDescriptiveStatistics import return_25th_quantile
import pandas as pd
from math import floor


def test_return_25th_quantile():
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    target_column = 'sepal_width'

    res =  return_25th_quantile(data, target_column)
    
    # hand calculations
    data = data.sort_values(by=target_column)
    quan_25th = data.iloc[floor(data.shape[0] / 4)][target_column]
 
    assert res == quan_25th
