#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your dataset has a 'month' column and is loaded as df
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv' 
df = pd.read_csv(data_path)

# Optional: If your dataset does not categorize months into seasons, you might add a mapping from months to seasons
# month_to_season = {
#     1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
#     6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall', 
#     11: 'Fall', 12: 'Winter'
# }
# df['season'] = df['month'].map(month_to_season)

# Aggregate the data by month (or season if you prefer)
suicide_rates_by_month = df.groupby('month')['suicides/100k pop'].mean().reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Create a line plot (or bar plot) to visualize the average suicide rates by month
sns.lineplot(x='month', y='suicides/100k pop', data=suicide_rates_by_month, marker='o')

plt.title('Average Suicide Rates by Month')
plt.xlabel('Month')
plt.ylabel('Average Suicide Rate (per 100k population)')

plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  # Adjust if using seasons
plt.show()


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame and it includes a column named 'date'
# First, ensure the date column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract the month from the date column (replace 'date' with the actual name of your date column)
df['month'] = df['date'].dt.month

# Optional: Map months to seasons if preferred
# Define a simple function to map month to season
def month_to_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    
df['season'] = df['month'].apply(month_to_season)

# Now, proceed with your analysis, using 'month' or 'season' for grouping
suicide_rates_by_time = df.groupby('season')['suicides/100k pop'].mean().reset_index()  # Or group by 'month'

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Adjust the x and y according to whether you're plotting by month or season
sns.barplot(x='season', y='suicides/100k pop', data=suicide_rates_by_time, palette='coolwarm')

plt.title('Average Suicide Rates by Season')
plt.xlabel('Season')
plt.ylabel('Average Suicide Rate (per 100k population)')

plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct the path to your dataset
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'
df = pd.read_csv(data_path)

# Assuming your DataFrame 'df' includes a column for the month (if not, you'll need to extract it from a date column)
# If you have a date column, you'll first convert it to datetime and then extract the month:
# df['date'] = pd.to_datetime(df['date'])
# df['month'] = df['date'].dt.month

# Calculate the average suicide rate by month
suicide_rates_by_month = df.groupby('month')['suicides/100k pop'].mean().reset_index()

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Assuming 'month' is a numerical column that represents the month of the year, 1 through 12
sns.lineplot(x='month', y='suicides/100k pop', data=suicide_rates_by_month, marker='o')

plt.title('Seasonal Variation in Suicide Rates')
plt.xlabel('Month')
plt.ylabel('Average Suicide Rate (per 100k population)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.show()


# In[4]:


import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetics for the plots
sns.set(style="whitegrid")

# Plotting the trend of suicide rates over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_uploaded, x="year", y="suicides/100k pop", estimator="mean", ci=None, marker="o")
plt.title('Trend of Suicide Rates Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Suicide Rate per 100k Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = r'C:\Users\THUSHAR\OneDrive\Desktop\cleaned_suicide_data_set cleaned.csv'  # Make sure to replace this with the actual path to your dataset
df_uploaded = pd.read_csv(data_path)

# Set the aesthetics for the plots
sns.set(style="whitegrid")

# Plotting the trend of suicide rates over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_uploaded, x="year", y="suicides/100k pop", estimator="mean", ci=None, marker="o")
plt.title('Trend of Suicide Rates Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Suicide Rate per 100k Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns

# Ensure that the dataframe is loaded as df_uploaded
# Assuming df_uploaded is already loaded from previous steps

# Enhancing the plot aesthetics using seaborn
sns.set(style="whitegrid", palette="muted")

# Create a larger plot
plt.figure(figsize=(14, 8))

# Plotting the line
line = sns.lineplot(data=df_uploaded, x="year", y="suicides/100k pop", estimator="mean", ci=None, color="skyblue", label='Trend')

# Highlighting each year with a scatter plot
scatter = sns.scatterplot(data=df_uploaded, x="year", y="suicides/100k pop", estimator="mean", ci=None, color="red", edgecolor="w", s=100, label='Yearly Data')

plt.title('Trend of Suicide Rates Over the Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Suicide Rate per 100k Population', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()


# In[ ]:




