import matplotlib.pyplot as plt
import seaborn as sns

def outliers(dataframe, column):
    '''
    This function returns all the outliers from a column in a dataframe, where values 
    are outside of range(q1 - (1.5 * IQR), q3 + (1.5 * IQR)).
    '''
    outliers = []
    q1 = np.percentile(sorted(dataframe[column]), 25)
    q3 = np.percentile(sorted(dataframe[column]), 75)
    IQR = q3 - q1
    lwr_bound = q1 - (1.5 * IQR)
    upr_bound = q3 + (1.5 * IQR)
    for i in sorted(dataframe[column]): 
        if (i < lwr_bound or i > upr_bound):
            outliers.append(i)
    return outliers, lwr_bound, upr_bound

def extended_describe(dataframe, columns):
    '''
    This function returns a dataframe with extended statistics to the chosen, numerical columns;
    It is similat do pd.describe, but includes more metrics.
    '''
    ed = pd.DataFrame({'Mean': dataframe[columns].mean(),
                       'Standard deviation': dataframe[columns].std(),
                       'Median': dataframe[columns].median(),
                       'Sum': [dataframe[c].sum() for c in columns],
                       'Skewness': [skew(dataframe[c]) for c in columns],
                       'Kurtosis': [kurtosis(dataframe[c]) for c in columns],
                       'Outliers count': [len(outliers(dataframe, c)[0]) for c in columns],
                      'IQR Lower bound': [outliers(dataframe, c)[1] for c in columns],
                      'IQR Upper bound': [outliers(dataframe, c)[2] for c in columns]})

    return ed.T

def count_orders(dataframe, column, dictionary=None):
    '''
    This function returns count of the orders for a categorical data.
    '''
    orders = dataframe[column].value_counts(ascending=False)
    if dictionary:
        orders.index = orders.index.map(dictionary)
    return orders

def count_items_ordered(dataframe, column, dictionary=None):
    '''
    This function returns count of item ordered for a categorical data.
    '''
    items = dataframe.groupby(column)['Order_Item_Quantity'].sum().sort_values(ascending=False)
    if dictionary:
        items.index = items.index.map(dictionary)
    return items