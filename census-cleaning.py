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

def remove_commas(df):
    df = df.apply(lambda x: x.str.replace(',', ''))
    return df

def print_head(df):
    print(df.head())

def save_cleaned_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-cleaned.csv', index=False)
    return df

if __name__ in '__main__':
    df = load_data()
    rc = remove_commas(df)
    save_cleaned_data(rc)



