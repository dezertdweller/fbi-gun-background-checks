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

if __name__ in '__main__':
   df = convert_to_csv()
   df = load_data()