# import liblaries
import numpy as np
import pandas as pd
import pickle

# load in the data (available on Kaggle in readme, could not fit my repository, I am using locally)
df = pd.read_parquet("data/DataCoSupplyChainDataset.parquet")

# create dictionaries encoded data and save to file
def create_dictionary(df, column1, column2):
    dict_name = {}
    for i, j in zip(df[column1].unique(), df[column2].unique()):
        dict_name[i] = j
    return dict_name

product_name = create_dictionary(df, 'Product Card Id', 'Product Name')
department_name = create_dictionary(df, 'Department Id', 'Department Name')
category_name = create_dictionary(df, 'Category Id', 'Category Name')

with open('data/supply_chain_dictionaties.pkl', 'wb') as f:
    pickle.dump((product_name, department_name, category_name), f)

# create locations dataset
store_locations_df = pd.DataFrame({'Latitude': df['Latitude'],
                                   'Longitude': df['Longitude']})
store_locations_df = store_locations_df.drop_duplicates()

store_locations_df.to_parquet('data/store_locations.parquet', index=False)


# delete unnessesary columns
df = df.drop(['Customer Email', 'Customer Fname', 'Customer Lname',
              'Customer Password', 'Customer Street', 'Customer Zipcode',
              'Order Zipcode', 'Product Description', 'Product Image',
              'Product Category Id', 'Category Name', 'Department Name',
              'Order Customer Id','Order Item Cardprod Id', 'Product Name',
             'Latitude', 'Longitude', 'Delivery Status', 'Late_delivery_risk',
             'Order City', 'Product Status', 'Order State'], axis=1)

# rounding up the large float values 
decimals = pd.Series([3, 3, 3, 3, 3], index=['Benefit per order', 'Sales per customer', 
                                             'Order Item Discount', 'Order Item Total',
                                             'Order Profit Per Order'])
df = df.round(decimals)

# dealing with datetime columns 

df = df.rename(columns={'shipping date (DateOrders)': 'Shipping date',
                       'order date (DateOrders)': 'Order date'})

df['Shipping date'] = pd.to_datetime(df['Shipping date'],errors = 'coerce', dayfirst=True)
df['Order date'] = pd.to_datetime(df['Order date'],errors = 'coerce', dayfirst=True)
# tu są jakieś błędy!
df['Shipping time'] = pd.to_datetime(df['Shipping date'], format='%H:%M')
df['Shipping day'] = df['Shipping date'].dt.day_name()


df['Order time'] = pd.to_datetime(df['Order date'], format='%H:%M')
df['Order day'] = df['Order date'].dt.day_name()


# feature engineering -> create a column representing the difference between expected and realistic shipping time

df['Target shipping days'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']
df = df.drop(['Days for shipping (real)', 'Days for shipment (scheduled)'], axis=1)

# changing the datatype for numeric valeus that should not be calculated
id_values = ['Category Id', 'Customer Id','Department Id', 'Order Id', 'Order Item Id', 'Product Card Id']
df[id_values] = df[id_values].astype('category')

# save the final df
df.to_parquet('data/SupplyChainDataset_cleaned.parquet', index=False)