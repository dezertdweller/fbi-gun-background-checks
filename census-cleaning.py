# New file for the script I will use to clean my Census data file.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

sns.set_style('darkgrid')

def load_data():
    df = pd.read_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data.csv')
    return df

def print_head(df):
    print(df.head())

def remove_commas(df):
    for col in df.columns[1:]: #Exclude 'Fact' column
        df[col] = df[col].str.replace(',', '')
    return df

def convert_percentages(x):
     if isinstance(x, str):
        x = x.strip()
        if "%" in x:
            if x.startswith("-"):
                return -float(x.replace("-", "").replace("%", "")) / 100
            else:
                return float(x.replace("%", "")) / 100
     return x

"""This function is designed to operate on an individual cell of the DataFrame, 
not the entire DataFrame at once. To convert all percentages in the DataFrame, 
I need to  apply this function to each cell in the DataFrame, which can be done 
with the applymap() function in if __name..."""

def save_cleaned_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-cleaned.csv', index=False)
    return df

if __name__ in '__main__':
    df = load_data()
    rc = remove_commas(df)
    cp = df.applymap(convert_percentages)
    print_head(cp)
    save_cleaned_data(cp)



