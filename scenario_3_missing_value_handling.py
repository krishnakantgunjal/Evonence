# Scenario 3: Missing Value Handling
# Task: A dataset has missing values in the "income" column. Write code to:

# 1. Replace missing values with the median if the data is normally distributed.

# 2. Replace with the mode if skewed.
# Use Pandas and a skewness threshold of 0.5.

import pandas as pd

def handle_missing_values(df):
    skewness = df["income"].skew()

    if abs(skewness) < 0.5:
        df["income"].fillna(df["income"].median(), inplace=True)
    else:
        df["income"].fillna(df["income"].mode()[0], inplace=True)

    return df

data = {"income": [50000, None, 60000, None, 70000]}
df = pd.DataFrame(data)

print(handle_missing_values(df))