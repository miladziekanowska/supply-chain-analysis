# import liblaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm

# load in the data
df = pd.read_csv('data/DataCoSupplyChainDataset.csv', sep=';')

# create dictionaries encoded data
def create_dictionary(df, column1, column2):
    dict_name = {}
    for i, j in zip(df[column1].unique(), df[column2].unique()):
        dict_name[i] = j
    return dict_name

product_name = create_dictionary(df, 'Product Card Id', 'Product Name')
department_name = create_dictionary(df, 'Department Id', 'Department Name')
category_name = create_dictionary(df, 'Category Id', 'Category Name')

# delete unnessesary columns
df = df.drop(['Customer Email', 'Customer Fname', 'Customer Lname',
              'Customer Password', 'Customer Street', 'Customer Zipcode',
              'Order Zipcode', 'Product Description', 'Product Image',
              'Product Category Id', 'Category Name', 'Department Name',
              'Order Customer Id','Order Item Cardprod Id', 'Product Name'], axis=1)

#dealing with the shipping and order date columns
df = df.rename(columns={'shipping date (DateOrders)': 'Shipping date',
                       'order date (DateOrders)': 'Order date'})

df['Shipping date'] = pd.to_datetime(df['Shipping date'],errors = 'coerce', dayfirst=True)
df['Order date'] = pd.to_datetime(df['Order date'],errors = 'coerce', dayfirst=True)

df['Shipping time'] = pd.to_datetime(df['Shipping date'].dt.strftime('%H:%M'), errors = 'coerce', dayfirst=True)
df['Shipping day'] = pd.to_datetime(df['Shipping date'].dt.date,errors = 'coerce', dayfirst=True)

df['Order time'] = pd.to_datetime(df['Order date'].dt.strftime('%H:%M'),errors = 'coerce', dayfirst=True)
df['Order day'] = pd.to_datetime(df['Order date'].dt.date,errors = 'coerce', dayfirst=True)

df = df.drop(['Shipping date', 'Order date'], axis=1)

# feature engineering -> create a column representing the difference between expected and realistic shipping time

df['Target shipping days'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']