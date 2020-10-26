#!/usr/bin/env python
# coding: utf-8

# # Splendor Analysis
# In this notebook we will be analysing the balance of the board game Splendor, and looking for anything that could be used as an advantage while playing the game.

# ## Imports

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


url_for_card_data = 'https://docs.google.com/spreadsheets/d/1N0PER6jcTOEE6P_r6UZAlaD2XOAAwShXhSk1wL76oys/edit?usp=sharing'


# In[3]:


df = pd.read_html(url_for_card_data)[0]


# In[4]:


df.head()


# In[5]:


df.info()


# ## Data Cleaning
# sprucing up the dataframe.

# In[6]:


df.columns


# In[7]:


trimed_df = df.loc[:91,'A':'H'].copy()
trimed_df.info()


# In[8]:


trimed_df.head()


# In[9]:


column_list = list(trimed_df.loc[0])[:]


# In[14]:


cards = trimed_df.loc[1:90,:]


# In[15]:


cards.columns = column_list


# In[16]:


cards.info()


# In[ ]:




