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

# create locations dataset
store_locations_df = pd.DataFrame({'Latitude': df['Latitude'],
                                   'Longitude': df['Longitude']})
store_locations_df = store_locations_df.drop_duplicates()


# delete unnessesary columns
df = df.drop(['Customer Email', 'Customer Fname', 'Customer Lname',
              'Customer Password', 'Customer Street', 'Customer Zipcode',
              'Order Zipcode', 'Product Description', 'Product Image',
              'Product Category Id', 'Category Name', 'Department Name',
              'Order Customer Id','Order Item Cardprod Id', 'Product Name',
             'Latitude', 'Longitude', 'Delivery Status', 'Late_delivery_risk',
             'Order City', 'Sales', 'Product Status'], axis=1)

# rounding up the large float values 
decimals = pd.Series([3, 3, 3, 3, 3], index=['Benefit per order', 'Sales per customer', 'Order Item Discount', 'Order Item Total',
            'Order Profit Per Order'])
df = df.round(decimals)

# dealing with datetime columns 
""" 
NOTE: This part would take place with the data cleaning, however due to the size of the file it would exceed github's
      requirements and not be uploaded. When working on local directory, please uncomment this part and use with 
      the data cleaning.
      

df = df.rename(columns={'shipping date (DateOrders)': 'Shipping date',
                       'order date (DateOrders)': 'Order date'})

df['Shipping date'] = pd.to_datetime(df['Shipping date'],errors = 'coerce', dayfirst=True)
df['Order date'] = pd.to_datetime(df['Order date'],errors = 'coerce', dayfirst=True)

df['Shipping time'] = pd.to_datetime(df['Shipping date'].dt.strftime('%H:%M'), errors = 'coerce', dayfirst=True)
df['Shipping day'] = pd.to_datetime(df['Shipping date'].dt.date,errors = 'coerce', dayfirst=True)
df['Shipping day'] = df['Shipping date'].dt.day_name()

df['Order time'] = pd.to_datetime(df['Order date'].dt.strftime('%H:%M'),errors = 'coerce', dayfirst=True)
df['Order day'] = pd.to_datetime(df['Order date'].dt.date,errors = 'coerce', dayfirst=True)
df['Order day'] = df['Order date'].dt.day_name()

df = df.drop(['Shipping date', 'Order date'], axis=1)

# feature engineering -> create a column representing the difference between expected and realistic shipping time

df['Target shipping days'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']

"""


df.to_csv('data/supply_chain_cleaned.csv')