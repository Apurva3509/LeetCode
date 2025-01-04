import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    return pd.DataFrame({'SecondHighestSalary': [np.nan if salaries.size < 2 else salaries.iloc[1]]})