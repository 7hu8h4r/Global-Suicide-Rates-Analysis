#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming df_uploaded is your loaded dataset
# Calculate the average suicide rate per country
average_suicide_rates_by_country = df_uploaded.groupby('country')['suicides/100k pop'].mean().sort_values(ascending=False).reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 20))

# Create a bar plot to visualize the average suicide rates by country
sns.barplot(x='suicides/100k pop', y='country', data=average_suicide_rates_by_country, palette='coolwarm')

plt.title('Average Suicide Rates by Country')
plt.xlabel('Average Suicide Rate (per 100k population)')
plt.ylabel('Country')

plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset again
data_path = '/mnt/data/cleaned_suicide_data_set cleaned.csv'
df = pd.read_csv(data_path)

# Calculate the average suicide rate per country
average_suicide_rates_by_country = df.groupby('country')['suicides/100k pop'].mean().sort_values(ascending=False).reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 20))

# Create a bar plot to visualize the average suicide rates by country
sns.barplot(x='suicides/100k pop', y='country', data=average_suicide_rates_by_country, palette='coolwarm')

plt.title('Average Suicide Rates by Country')
plt.xlabel('Average Suicide Rate (per 100k population)')
plt.ylabel('Country')

plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset again
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'
df = pd.read_csv(data_path)

# Calculate the average suicide rate per country
average_suicide_rates_by_country = df.groupby('country')['suicides/100k pop'].mean().sort_values(ascending=False).reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 20))

# Create a bar plot to visualize the average suicide rates by country
sns.barplot(x='suicides/100k pop', y='country', data=average_suicide_rates_by_country, palette='coolwarm')

plt.title('Average Suicide Rates by Country')
plt.xlabel('Average Suicide Rate (per 100k population)')
plt.ylabel('Country')

plt.show()


# In[ ]:




