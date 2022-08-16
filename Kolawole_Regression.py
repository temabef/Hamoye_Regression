#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load CSV


# In[2]:


import pandas as pd


# In[10]:


import matplotlib.pyplot as plt


# In[8]:


dataset = pd.read_csv("energydata_complete.csv")


# In[9]:


dataset.head()


# In[11]:


dataset.corr()


# In[ ]:




