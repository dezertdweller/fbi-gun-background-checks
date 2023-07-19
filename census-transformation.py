import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

sns.set_style('darkgrid')

def load_data():
    df = pd.read_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-cleaned.csv')
    return df

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

def transform_data(df):
    df = df.set_index('Fact').transpose().reset_index()
    df = df.rename(columns={'index': 'State'})
    return df

def simplify_data(df):
    df = df.rename(columns = {
         'Population estimates, July 1, 2016,  (V2016)':'Population 2016', 
         'Population, percent change - April 1, 2010 (estimates base) to July 1, 2016,  (V2016)':'Population Percent Change 2010-2016', 
         'Persons under 5 years, percent, July 1, 2016,  (V2016)':'Under 5',
         'Persons under 18 years, percent, July 1, 2016,  (V2016)':'Under 18',
         'Persons 65 years and over, percent,  July 1, 2016,  (V2016)':'65 and over',
         'Female persons, percent,  July 1, 2016,  (V2016)':'Percent Female',
         'Population, Census, April 1, 2010':'Population 2010','Black or African American alone, percent, July 1, 2016,  (V2016)':'Percent Black',
         'American Indian and Alaska Native alone, percent, July 1, 2016,  (V2016)':'Percent American Indian',
         'Asian alone, percent, July 1, 2016,  (V2016)':'Percent Asian',
         'Native Hawaiian and Other Pacific Islander alone, percent, July 1, 2016,  (V2016)':'Percent Native Hawaiian',
         'Two or More Races, percent, July 1, 2016,  (V2016)':'Percent Two or More Races',
         'Hispanic or Latino, percent, July 1, 2016,  (V2016)':'Percent Latine',
         'White alone, not Hispanic or Latino, percent, July 1, 2016,  (V2016)':'Percent White',
         'Veterans, 2011-2015':'Veterans',
         'Foreign born persons, percent, 2011-2015':'Foreign Born Percent',
         'Housing units,  July 1, 2016,  (V2016)':'Housing Units 2016',
         'Households, 2011-2015':'Households',
         'Persons per household, 2011-2015':'Persons per Household', 
         'Language other than English spoken at home, percent of persons age 5 years+, 2011-2015':'Other Langague at Home',
         'High school graduate or higher, percent of persons age 25 years+, 2011-2015':'Percent Graduated High School or Higher', 
         'Bachelor\'s degree or higher, percent of persons age 25 years+, 2011-2015':'Percent Bachelor\'s Degree or Higher',
         'With a disability, under age 65 years, percent, 2011-2015':'Percent Disability Under 65', 
         'Persons  without health insurance, under age 65 years, percent':'Under 65 Uninsured Percent', 
         'In civilian labor force, total, percent of population age 16 years+, 2011-2015':'Percent in Workforce',
         'Median household income (in 2015 dollars), 2011-2015':'Median Household Income',
         'Per capita income in past 12 months (in 2015 dollars), 2011-2015':'Per Capita Income',
         'Persons in poverty, percent':'Percent Poverty',
         'Total employer establishments, 2015':'Total Employer Establishments',
         'Total employment, 2015':'Total Employment',
         'Population per square mile, 2010':'Population per Square Mile'
    })
    
    df = df.drop([
                'Persons under 5 years, percent, April 1, 2010',
                'Persons under 18 years, percent, April 1, 2010',
                'Persons 65 years and over, percent, April 1, 2010', 
                'Female persons, percent, April 1, 2010',
                'Housing units, April 1, 2010',
                'White alone, percent, July 1, 2016,  (V2016)',
                'Owner-occupied housing unit rate, 2011-2015',
                'Median value of owner-occupied housing units, 2011-2015',
                'Median selected monthly owner costs -with a mortgage, 2011-2015',
                'Median selected monthly owner costs -without a mortgage, 2011-2015', 
                'Median gross rent, 2011-2015', 
                'Building permits, 2016',
                'Living in same house 1 year ago, percent of persons age 1 year+, 2011-2015',
                'In civilian labor force, female, percent of population age 16 years+, 2011-2015',
                'Total accommodation and food services sales, 2012 ($1,000)',
                'Total health care and social assistance receipts/revenue, 2012 ($1,000)',
                'Total manufacturers shipments, 2012 ($1,000)', 
                'Total merchant wholesaler sales, 2012 ($1,000)',
                'Total retail sales, 2012 ($1,000)',
                'Total retail sales per capita, 2012',
                'Mean travel time to work (minutes), workers age 16 years+, 2011-2015',
                'Total annual payroll, 2015 ($1,000)',
                'Total employment, percent change, 2014-2015', 
                'Total nonemployer establishments, 2015',
                'All firms, 2012', 
                'Men-owned firms, 2012',
                'Women-owned firms, 2012', 
                'Minority-owned firms, 2012', 
                'Nonminority-owned firms, 2012',
                'Veteran-owned firms, 2012',
                'Nonveteran-owned firms, 2012', 
                'Land area in square miles, 2010'
        ], axis=1)

    return df

def round_numbers(df):
    df = df.round(3)
    return df

def save_transformed_data(df):
    df = df.to_csv('/Users/katialopes-gilbert/data-files/ncis-and-census-data/us-census-data-transformed.csv', index=False)
    return df

if __name__ in '__main__':
    df = load_data()
    df = remove_rows_and_columns(df)
    df = transform_data(df)
    df = simplify_data(df)
    df = round_numbers(df)
    save_transformed_data(df)