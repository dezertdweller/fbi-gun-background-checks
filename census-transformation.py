import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

sns.set_style('darkgrid')

def load_data():
    df = pd.read_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-cleaned.csv')
    return df

def print_head(df):
    print(df.head())

def print_info(df):
    print(df.info())

def remove_rows_and_columns(df):
    # Remove columns
    df = df.drop(['Fact Note'], axis=1)
    
    # Remove rows
    unwanted_rows = ['FIPS Code', 'nan', 'NOTE: FIPS Code values are enclosed in quotes to ensure leading zeros remain intact.', 
                     'Value Notes', '1', 'Fact Notes', '(a)', '(b)', '(c)', 
                     'Value Flags', '-', 'D', 'F', 'FN', 'S', 'X', 'Z']
    df = df[~df['Fact'].isin(unwanted_rows)]

    # Remove null rows
    df = df.dropna(how='all')

    return df
    
def save_transformed_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-transformed.csv', index=False)
    return df

if __name__ in '__main__':
    df = load_data()
    df = remove_rows_and_columns(df)
    print_head(df)
    print_info(df)
    save_transformed_data(df)