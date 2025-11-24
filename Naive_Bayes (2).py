#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('Book1.csv')


# In[3]:


df


# In[4]:


pd.crosstab(df['Outlook'], df['Class'],normalize='columns').stack().to_dict()


# In[6]:


D = {}
for i in ['Outlook','Temperature',	'Humidity',	'Windy']:
  D.update(pd.crosstab(df[i], df['Class'],normalize='columns').stack().to_dict())


# In[7]:


D


# In[ ]:




