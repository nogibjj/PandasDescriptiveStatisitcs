# Pandas Descriptive Statistics Script
## Week 2 Mini Project by Rakeen Rouf

[![PythonCiCd](https://github.com/rmr327/cicd_python_template/actions/workflows/python_ci_cd.yml/badge.svg)](https://github.com/rmr327/cicd_python_template/actions/workflows/python_ci_cd.yml)

---

**Summary**

The objective of this week's mini project was to create a script utilizing pandas for descriptive statistics. This script has been integrated with the Python CiCd automation template introduced in week one.

---

**Code Location**

You can find the relevant code in the following folders:
- `src`
- `test`

---

**Function Descriptions**

1. `def return_25th_quantile(df: pd.DataFrame, target: str) -> float:`  
   Takes a dataframe and returns the 25th quantile of the user defined target column.

2. `def return_mean(data_: pd.DataFrame, target: str) -> float`  
   Takes in a dataframe and returns the mean of the user defined target column.

3. `def return_std_dev(data_: pd.DataFrame, target: str) -> float`  
   Takes in a dataframe and returns the standard deviation of the user defined target column.

4. `def return_median(data_: pd.DataFrame, target: str) -> float`  
   Takes in a dataframe and returns the mean of the user defined target column.

5. `def visualize_dataset(data_: pd.DataFrame, outcome_var: str, target_var: str, inteaction_term: str) -> None`  
   Visualizes the passed data. Makes a scatter plot of target vs outcome variables. Colors the scatter
   plot by the interaction term. Draws a best fit linear regression line for each category of the iinteration
   term. Draws vertical lines to signify the mean, median and standard deviation.

---

**Sample Visualization Using the IRIS data set**

![Visualization Example](https://user-images.githubusercontent.com/36940292/266804593-4fe25e4a-186c-4e49-956a-508c5d66cb05.jpg)
---
Feel free to explore the code and tests in the respective folders.
