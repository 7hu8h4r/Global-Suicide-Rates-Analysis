#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(14, 8))

# Grouped bar chart for generational suicide rates
sns.barplot(x='year', y='suicides/100k pop', hue='generation', data=data, ci=None, palette='deep')
plt.title('Comparative Suicide Rates by Generation Over Years')
plt.xlabel('Year')
plt.ylabel('Suicides per 100k Population')
plt.legend(title='Generation', loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv(r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv')  # Replace 'path_to_your_dataset.csv' with the actual path to your dataset

plt.figure(figsize=(14, 8))

# Grouped bar chart for generational suicide rates
sns.barplot(x='year', y='suicides/100k pop', hue='generation', data=data, ci=None, palette='deep')
plt.title('Comparative Suicide Rates by Generation Over Years')
plt.xlabel('Year')
plt.ylabel('Suicides per 100k Population')
plt.legend(title='Generation', loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# In[ ]:




