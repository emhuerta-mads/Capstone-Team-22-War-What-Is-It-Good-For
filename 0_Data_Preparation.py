#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries
import pandas as pd
import numpy as np
from datetime import datetime
import csv


# In[2]:


# Import Datasets
dataset_dict = {'CPIAUCSL':'cpi_df','GDP':'gdp_df', 'FEDREV':'fedrev_df', 'PCE':'pce_df', 
    'FEDFUNDS':'fedfunds_df', 'GFDEBTN':'feddebt_df', 'PSAVERT':'psave_df', 
    'REVOLSL':'revolcredit_df', 'UNRATE':'unemploy_df'}


# In[3]:


# Create Individual Datasets
for k, v in dataset_dict.items():
    globals()[v] = pd.read_csv('./Data/{}.csv'.format(k))


# In[4]:


# Transform Datasets
# Rename Columns: CPI, FEDREV
cpi_df = cpi_df.rename(columns={'CPIAUCSL': 'CPI'})
fedrev_df = fedrev_df.rename(columns={'Total Direct Revenue - Federal $ million nominal': 'FEDREV_mm_nom'})

# Transform Dataset: FEDREV
# Create YYYY-MM-DD Date Column
fedrev_df['DATE'] = fedrev_df['Year'] # + 1
fedrev_df['DATE'] = fedrev_df['DATE'].astype(str)
fedrev_df['DATE'] = fedrev_df['DATE'] + '-01-01'
fedrev_df = fedrev_df[['DATE', 'FEDREV_mm_nom']]

# Create Dataset: INFL: Inflation
# Calculate 12 month lag for later inflation % calculations
cpi_df['lag_12_diff'] = cpi_df['CPI'].diff(periods=12)
cpi_df['lag_12'] = cpi_df['CPI'] - cpi_df['lag_12_diff']
cpi_df['INFL'] = (cpi_df['lag_12_diff'] / cpi_df['lag_12']) * 100

# INF: Inflation
infl_df = cpi_df[['DATE', 'INFL']].dropna()
cpi_df = cpi_df[['DATE', 'CPI']]

# Add INFL to dataset_dict
dataset_dict['INFL'] = 'infl_df'


# In[5]:


# Create Merged Dataset
dates_lst = []
[dates_lst.extend(globals()[v].iloc[:,0]) for k, v in dataset_dict.items()]
dates_lst = list(set(dates_lst))
dates_lst.sort()

merged_df = pd.DataFrame(dates_lst, columns=['DATE'])
for k, v in dataset_dict.items():
    merged_df = merged_df.merge(globals()[v], on='DATE', how='outer')


# In[6]:


# Save Datasets to CSV
merged_df.to_csv('./Data/merged_df.csv', index=False)   
infl_df.to_csv('./Data/INFL.csv', index=False)  

# Add 3 Global Variables
global cc_outstanding_df, war_timeline_df, war_dates_df

# Store Variables
# dataset_dict.values()
get_ipython().run_line_magic('store', 'cpi_df gdp_df fedrev_df pce_df fedfunds_df feddebt_df psave_df revolcredit_df unemploy_df infl_df cc_outstanding_df merged_df dataset_dict war_timeline_df war_dates_df')


