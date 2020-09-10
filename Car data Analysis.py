#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


car = pd.read_csv(r'D:\DataSets\Cars Data.csv')


# In[6]:


car


# In[8]:


car.shape


# In[13]:


car.isnull().sum()


# In[19]:


null_columns=car.columns[car.isnull().any()]
null_columns


# In[20]:


[car[car.isnull().any(axis=1)][null_columns].head()]


# In[23]:


car.dropna(axis=0,inplace=True)
car.head(40)


# In[25]:


car['Make'].nunique()


# In[26]:


car['Make'].value_counts()


# In[27]:


car.head()


# In[41]:


# car[(car.Origin == 'Asia') | (car.Origin == 'Europe')]
car[car.Origin.isin(['Asia','Europe'])]


# In[34]:


column_names = car.columns
column_names


# In[35]:



new_frame = car.loc[:, column_names]


# In[36]:


new_frame


# car_Europe = car[car.Origin == 'Europe']
# car_Europe.Make.value_counts()

# # Remove all the instances where Weight is greater than 4000

# In[45]:


car[~(car.Weight>4000)]


# In[ ]:




