#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

dataframe = pd.read_csv("database.csv")

top_5 = dataframe.head(5)
print(top_5)
name = top_5['country/organization Name']
number = top_5["Satellites in Orbit"]

plt.xlabel("country/organization Name")
plt.xticks(rotation='vertical')
plt.ylabel("Satellites in Orbit")

label = name
value = number
plt.bar(label, value,width=0.4, color=('blue','purple','orange','pink','red'))#gar-graph


# In[ ]:





# In[ ]:




