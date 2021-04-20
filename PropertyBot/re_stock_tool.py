#!/usr/bin/env python
# coding: utf-8

# # DataFrames
# 
# DataFrames are the workhorse of pandas and are directly inspired by the R programming language. We can think of a DataFrame as a bunch of Series objects put together to share the same index. Let's use pandas to explore this topic!

# ## Data Prep

# In[20]:


import pandas as pd
import scipy as sp
import numpy as np
from pandas_datareader import data as pdr
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.linalg import inv, pinv


# In[21]:


HOME_PRICE_CSV = 'raw_home_values_metro_3_bedroom'
HOME_RENT_CSV = 'raw_home_rents_metro'


def prep_zillow(mycsv,value_name):
    df = pd.read_csv('data/{0}.csv'.format(mycsv), encoding = "ISO-8859-1")
    
    df = df.drop('RegionID', axis=1)
    df = df.drop('RegionType', axis=1)
    df = df.drop('StateName', axis=1)

    df = df.melt(id_vars=['RegionName','SizeRank'], 
                             var_name='Year_Month', 
                             value_name=value_name
                            )
    df = df.set_index(['RegionName','SizeRank', 'Year_Month'])
    df.sort_index(inplace=True)
    return df


# In[22]:


def get_sp_500():
    sp500 = pdr.get_data_yahoo('^GSPC')
    sp500['year'] = sp500.index.year
    sp500['month'] = sp500.index.month
    return sp500


# In[23]:


def total_return(prices):
    """Retuns the return between the first and last value of the DataFrame.
    Parameters
    ----------
    prices : pandas.Series or pandas.DataFrame
    Returns
    -------
    total_return : float or pandas.Series
        Depending on the input passed returns a float or a pandas.Series.
    """
    return prices.iloc[-1] / prices.iloc[0] - 1


# In[24]:


def merge_data(city):
    home_price = prep_zillow(mycsv=HOME_PRICE_CSV,value_name='home_price')
    home_rent = prep_zillow(mycsv=HOME_RENT_CSV,value_name='home_rent')
    homes = home_price.merge(home_rent, how = 'left', on=['RegionName', 'Year_Month','SizeRank'])
    homes.sort_index(inplace=True)
    homes = homes.fillna(0)
    # homes['adj_price'] = float(homes['home_price']) + float(homes['home_rent'])
    homes['adj_price'] = homes['home_price'].apply(lambda x: float(x))
    city = homes.loc[city]
    city = city.reset_index()
    city['return_realestate'] = (city.adj_price - city.adj_price.shift(1))/city.adj_price.shift(1)
    city['Year_Month'].loc[0].split("-")
    f = lambda x: x["Year_Month"].split("-")
    year_month = list(city.apply(f, axis=1))
    year_month = pd.DataFrame(year_month)
    year_month.columns = ['year', 'month']
    city = city.join(year_month, how='left')
    city.year = city.year.astype('int64')
    city.month = city.month.astype('int64')


    sp500 = get_sp_500()
    sp500 = pd.DataFrame(sp500.groupby(['year', 'month'], )['Adj Close'].apply(total_return))
    sp500['return_sp500'] = sp500['Adj Close']
    sp500 = sp500.reset_index()
    full_clean = city.merge(sp500, how='inner', left_on =['year','month'], right_on=['year', 'month'])
    final_clean = full_clean[['year', 'month', 'Metro', 'return_realestate', 'return_sp500']]
    return final_clean


# ## Modern Portfolio Theory

# In[38]:


def mpt(df, desired_returns):
    returns = df[['return_realestate', 'return_sp500']]
    R = np.array(returns)
    stockMean = np.mean(R, axis=0)
    n_stock = len(returns.columns)
    
    def objFunction(W, R, target_ret):
        stock_mean = np.mean(R, axis=0)
        port_mean = np.dot(W, stock_mean) # portfolio mean
        cov = np.cov(R.T) # var-cov matrix
        port_var = np.dot(np.dot(W, cov), W.T) # portfolio variance
        penalty = 2000*abs(port_mean-target_ret) # penalty for deviation
        return np.sqrt(port_var) + penalty #objective function
    
    out_mean, out_std, out_weight = [], [], []
    for r in np.linspace(np.min(stockMean), np.max(stockMean), num=100):
        W = np.ones([n_stock])/n_stock
        b_ = [(0,1), (0,1)]
        c_ = ({'type': 'eq', 'fun': lambda W: sum(W) - 1})
        for i in range(n_stock):
            result=sp.optimize.minimize(objFunction, W, (R, r), method='SLSQP', constraints=c_, bounds=b_)
            if not result.success: 
                BaseException(result.message)

            out_mean.append(round(r, 4))
            std_=round(np.std(np.sum(R*result.x, axis=1)), 6)
            out_std.append(std_)
            out_weight.append(result.x)
            
        mean = pd.DataFrame(out_mean) 
        std = pd.DataFrame(out_std)
        weight = pd.DataFrame(out_weight)
        result1 = pd.merge(mean, std, left_index=True, right_index=True)
        result2 = pd.merge(result1, weight, left_index=True, right_index=True)
        result2.columns = ['mean', 'std', 'weight_realestate', 'weight_stocks']
        result2 = result2.round(4)
        result2['annual_mean'] = (1 + result2['mean'])**12 - 1
    
  
    return result2.loc[(result2['annual_mean'] > desired_returns - .01) & (result2['annual_mean'] < desired_returns + .01)].describe().T
        


# In[26]:


def get_city_list():
    city_list = pd.read_csv('data/{0}.csv'.format(HOME_PRICE_CSV), encoding = "ISO-8859-1")
    return city_list['RegionName'].head(40)


# In[27]:


def main(city, desired_returns):
    return_data = merge_data(city=city)
    return mpt(df=return_data, desired_returns=desired_returns)


# In[28]:


def ui():
    print(get_city_list())
    city = input("City of Real Estate Investment (Single-Family Residence)):  ")
    desired_returns = float(input("What is your desired returns? Typically between 0.5 and .10 annually:  "))
    return main(city=city, desired_returns=desired_returns)
    


# In[29]:


ui()


# ## Analysis of Different Cities

# In[39]:


# main(city='Los Angeles', desired_returns=.08)


# # In[40]:


# main(city='Memphis', desired_returns=.08)


# In[ ]:




