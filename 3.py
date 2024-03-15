#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'  
df = pd.read_csv(data_path)

# Aggregate the data by age group
suicide_rates_by_age_group = df.groupby('age')['suicides/100k pop'].mean().reset_index().sort_values(by='suicides/100k pop', ascending=False)

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Create a bar plot to visualize the average suicide rates by age group
sns.barplot(x='suicides/100k pop', y='age', data=suicide_rates_by_age_group, palette='coolwarm')

plt.title('Average Suicide Rates by Age Group')
plt.xlabel('Average Suicide Rate (per 100k population)')
plt.ylabel('Age Group')

plt.show()


# In[ ]:




