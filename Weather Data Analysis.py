#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv(r'D:\DataSets\WeatherData.csv')

data
# In[5]:


data


# In[26]:


data.head(20)


# In[29]:


data.shape


# In[30]:


data.index


# In[35]:


data.columns


# In[38]:


data.isnull().sum()


# In[40]:


data.dtypes


# In[44]:


data['Weather'].nunique()


# In[45]:


data.nunique()

data.info()
# data['Weather'].value_counts()

# # Q1.Find all the Unique "wind Speed" values in data

# In[52]:


data['Wind Speed_km/h'].nunique()


# In[56]:


windspeed = data['Wind Speed_km/h'].unique()


# In[57]:


windspeed.sort()


# # Q2.How many times the weather was 'exactly clear'?
# 

# In[58]:


data['Weather'].nunique()


# In[59]:


data['Weather'].value_counts()


# In[63]:



# data.Weather=='Clear'
data[data.Weather == 'Clear']


# # Q3.Find the all the column where windspeed is 4km/h

# In[66]:


data[data['Wind Speed_km/h']==4]


# 
# # Q4.Rename wether into weather condition
# 

# In[13]:


data.rename(columns = {'Weather' :'weather condition'})


# 
# # What is the Mean of visibility?

# In[6]:


data['Visibility_km'].mean()


# 
# # What is the standard deviation of "Pressure"in this data?

# In[7]:


data.Press_kPa.std()


# # What is the variance of 'Relative humidity' in this data?

# In[8]:


data['Rel Hum_%'].var()


# # Find all instances when 'snow' was recorded?

# In[16]:


data.head(2)


# In[18]:


data[data['Weather'] == 'Snow']


# In[20]:


# For string Snow
data[data['Weather'].str.contains('Snow')]


# # Find all instances where Wind speed is above 24 and visibility is 25

# In[21]:


data.head(2)


# In[22]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# # What is the mean value of each colums aginst Weather?

# In[23]:


data.groupby('Weather').mean()


# # Find all instances where 
# weather is clear and Humidity is above 50
# or
# Visibility is above 40

# In[27]:


data[(data.Weather == 'Clear') & (data['Rel Hum_%']>50) | (data.Visibility_km>40)]


# In[ ]:




