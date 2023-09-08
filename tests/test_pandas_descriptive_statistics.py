"""Test script for pandas descriptive statistics script"""
import sys
from math import floor
import pandas as pd
sys.path.append("/workspaces/PandasDescriptiveStatisitcs")
from pandas_descriptive_statistics import return_25th_quantile


def test_return_25th_quantile():
    """test function"""
    data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    target_column = 'sepal_width'

    res =  return_25th_quantile(data, target_column)

    # hand calculations
    data = data.sort_values(by=target_column)
    quan_25th = data.iloc[floor(data.shape[0] / 4)][target_column]

    assert res == quan_25th
