#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'
data = pd.read_csv(dataset_path)

# Filter data for PCA (removing missing or infinite values)
economic_data = data[['gdp_per_capita ($)', 'suicides/100k pop']].dropna()

# Standardizing the features
x = economic_data.loc[:, ['gdp_per_capita ($)']].values
y = economic_data.loc[:, 'suicides/100k pop'].values
x = StandardScaler().fit_transform(x)

# PCA to reduce the dimensionality
pca = PCA(n_components=1)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, columns=['Principal Component'])

# Combine with suicide rates
finalDf = pd.concat([principalDf, economic_data[['suicides/100k pop']].reset_index(drop=True)], axis=1)

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Principal Component', y='suicides/100k pop', data=finalDf, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relationship between Economic Health (PCA) and Suicide Rates')
plt.xlabel('Composite Economic Index (Principal Component)')
plt.ylabel('Suicides per 100k Population')

plt.show()


# In[ ]:




