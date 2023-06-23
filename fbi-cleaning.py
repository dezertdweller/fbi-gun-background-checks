import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

sns.set_style('darkgrid')

def convert_to_csv():
    excel_file = '/Users/katialopes-gilbert/data-files/ncis-and-census-data/gun_data.xlsx'
    df = pd.read_excel(excel_file)

    csv_file = '/Users/katialopes-gilbert/data-files/ncis-and-census-data/gun_data.csv'
    df.to_csv(csv_file, index=False)

def load_data():
    df = pd.read_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/gun_data.csv')
    return df

def date_time(df):
    df['month'] = pd.to_datetime(df['month'])
    return df

def save_transformed_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/gun_data_clean.csv', index=False)
    return df

if __name__ in '__main__':
   df = convert_to_csv()
   df = load_data()
   df = date_time(df)
   df = save_transformed_data(df)