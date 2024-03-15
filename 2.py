#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data_path = 'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'  
df = pd.read_csv(data_path)

# Prepare the data: Calculate the average suicide rate per 100k for each gender across all years
suicide_rates_by_gender = df.groupby(['year', 'sex'])['suicides/100k pop'].mean().reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Create a box plot to visualize the distribution of suicide rates by gender
sns.boxplot(x='sex', y='suicides/100k pop', data=suicide_rates_by_gender)

plt.title('Distribution of Suicide Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Suicide Rate (per 100k population)')

plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct the path to your dataset using a raw string
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'
df = pd.read_csv(data_path)

# Prepare the data: Calculate the average suicide rate per 100k for each gender across all years
suicide_rates_by_gender = df.groupby(['year', 'sex'])['suicides/100k pop'].mean().reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Create a box plot to visualize the distribution of suicide rates by gender
sns.boxplot(x='sex', y='suicides/100k pop', data=suicide_rates_by_gender)

plt.title('Distribution of Suicide Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Suicide Rate (per 100k population)')

plt.show()


# In[ ]:




