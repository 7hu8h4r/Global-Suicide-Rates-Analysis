#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data_path = 'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'
df = pd.read_csv(data_path)

# Aggregate the data by year
suicides_per_year = df.groupby('year').agg(total_suicides=('suicides_no', 'sum'),
                                           suicide_rate=('suicides/100k pop', 'mean')).reset_index()

# Plotting
sns.set(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot total suicides on the first y-axis
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Suicides', color=color)
ax1.plot(suicides_per_year['year'], suicides_per_year['total_suicides'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for the suicide rate
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Suicide Rate (per 100k population)', color=color)
ax2.plot(suicides_per_year['year'], suicides_per_year['suicide_rate'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add a title and show the plot
plt.title('Suicide Trends Over Time')
fig.tight_layout()
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Corrected file path using a raw string to avoid escape sequence errors
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'

# Load the dataset
df = pd.read_csv(data_path)

# Aggregate the data by year
suicides_per_year = df.groupby('year').agg(total_suicides=('suicides_no', 'sum'),
                                           suicide_rate=('suicides/100k pop', 'mean')).reset_index()

# Plotting
sns.set(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot total suicides on the first y-axis
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Suicides', color=color)
ax1.plot(suicides_per_year['year'], suicides_per_year['total_suicides'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for the suicide rate
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Suicide Rate (per 100k population)', color=color)
ax2.plot(suicides_per_year['year'], suicides_per_year['suicide_rate'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add a title and show the plot
plt.title('Suicide Trends Over Time')
fig.tight_layout()
plt.show()


# In[ ]:




