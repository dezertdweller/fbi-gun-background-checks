import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

sns.set_style('darkgrid')

def load_data():
    df = pd.read_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-cleaned.csv')
    return df



def save_transformed_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-transformed.csv', index=False)
    return df

if __name__ in '__main__':
    df = load_data()
    save_transformed_data(df)