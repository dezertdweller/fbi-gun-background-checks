import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
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
    df.insert(1, 'year', df['month'].dt.year.astype(int))
    df.insert(1, 'month-name', df['month'].dt.strftime('%B'))
    return df

def drop_columns(df):
    columns_to_drop = ['permit', 'permit_recheck', 'admin', 'prepawn_handgun',
                   'prepawn_long_gun', 'prepawn_other', 'redemption_handgun',
                   'redemption_long_gun', 'redemption_other', 'returned_handgun',
                   'returned_long_gun', 'returned_other', 'rentals_handgun',
                   'rentals_long_gun', 'totals']

    df.drop(columns_to_drop, axis=1, inplace=True)
    return df

def sum_permits(df):
    columns_to_sum = ['handgun', 'long_gun', 'other', 'multiple', 'private_sale_handgun',
                  'private_sale_long_gun', 'private_sale_other', 'return_to_seller_handgun',
                  'return_to_seller_long_gun', 'return_to_seller_other']

    df['total_permits'] = df[columns_to_sum].sum(axis=1)
    return df

def save_transformed_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/gun_data_clean.csv', index=False)
    return df

if __name__ in '__main__':
   df = convert_to_csv()
   df = load_data()
   df = date_time(df)
   df = drop_columns(df)
   df = sum_permits(df)
   df = save_transformed_data(df)