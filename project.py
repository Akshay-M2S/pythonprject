#!/usr/bin/env python
# coding: utf-8

# ## Dataset on E-commerce Customer's purchases in Amazon.
# 

# 

# In[3]:


import pandas as pd
data=pd.read_csv('Ecommerce Purchases')
data.head()


# ## 1.Display Top 10 rows of dataset

# In[4]:


data.head(10)


# ##  2.Check last 10 rows of dataset

# In[5]:


data.tail(10)


# ## 3.Check Datatype of each column

# In[6]:


data.dtypes


# ## 4.Check null values in dataset

# In[8]:


data.isnull().sum()


# ## 5.Number of Rows and Columns  in our dataset

# In[9]:


data.info()


# ## 6.Highest and Lowest Purchase Price

# In[11]:


data.columns


# In[14]:


data['Purchase Price'].max()


# In[15]:


data['Purchase Price'].min()


# ## 7.Average Purchase Price

# In[16]:


data['Purchase Price'].mean()


# ##  8.How many people have french as their Language?

# In[22]:


len(data[data['Language']=='fr'])


# ## 9.Job Title containing IT sales professional

# In[32]:


data[data.Job=="IT sales professional"]


# ## 10.Find the E-mail of the persons having IP address: 156.210.0.254

# In[54]:


data[(data['IP Address']=='156.210.0.254')]["Email"]


# ## 11.How many people have Mastercard as their Credit card provider and made a purchase above 50

# In[59]:


len(data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"]>50)])


# ## 12.Find The Address of the with the following credit card number:5366164496542631

# In[62]:


data[data['Credit Card']==5366164496542631]['Address']


# ## 13.How many people purchase during AM and how many people purchase during PM?

# In[64]:


data["AM or PM"].value_counts()


# ## 14.How many people have a credit card that expires in 2021?

# In[69]:


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='21')])


# ## 15.Top  5 most popular Email providers (e.g. gmail.com,yahoo.com etc..)

# In[70]:


list1=[]
for email in data['Email']:
    list1.append(email.split('@')[1])


# In[72]:


data['temp']=list1


# In[73]:


data.head(1)


# In[76]:


data['temp'].value_counts().head(5)


# 

# In[ ]:





# In[ ]:




