import pandas as pd
from scipy.stats import ttest_ind

def hypothesis_tests(df):
    # Example: T-test for house age
    median_age = df['house age'].median()
    above_median_age = df[df['house age'] > median_age]['house price of unit area']
    below_median_age = df[df['house age'] <= median_age]['house price of unit area']
    t_statistic, p_value = ttest_ind(above_median_age, below_median_age)
    alpha = 0.05
    if p_value < alpha:
        print("The average price per unit area of houses above the median age is significantly different from those below the median age.")
    else:
        print("There is no significant difference in the average price per unit area of houses above the median age and those below the median age.")

if __name__ == "__main__":
    df = pd.read_csv('/content/cleaned_real_estate.csv')
    hypothesis_tests(df)
