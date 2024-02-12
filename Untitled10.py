#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[15]:


data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\spending.csv")
data.head(13)
#since this is a clean dataset we are not doing any cleaning


# In[23]:


plt.plot(data['Year'], data['PercentCelebrating'])
plt.xlabel('Year')
plt.ylabel('PercentCelebrating')
plt.title('People celebrating valentines day over the past few years')
plt.show()
#This graph shows us that the people are slowly neglecting valentine's day


# In[24]:


plt.plot(data['Year'], data['PerPerson'])
plt.xlabel('Year')
plt.ylabel('PerPerson')
plt.title('People spending per person')
plt.show()
#This graph shows us that the people are spending so much for what they don't even know who will become their partner.

