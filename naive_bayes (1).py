#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd


# In[11]:


df = pd.read_csv('Book1.csv')


# In[12]:


df


# In[13]:


pd.crosstab(df['Outlook'], df['Class'],normalize='columns').stack().to_dict()


# In[14]:


D = {}
for i in ['Outlook', 'Temperature', 'Humidity', 'Windy']:
    temp = pd.crosstab(df[i], df['Class'], normalize='columns').stack().to_dict()
   
    fixed_temp = {f"{k[0]}_{k[1]}": v for k, v in temp.items()}
    
    D.update(fixed_temp)



# In[15]:


D


# In[ ]:




