# Name: Muhammad Awais
# Student ID: 21084741

# In[19]:


# Loading data
import pandas as pd

data = pd.read_csv("API_19_DS2_en_csv_v2_4773766.csv", skiprows=4).iloc[:,:-1]
data.fillna(0, inplace=True)
data.head()


# In[20]:


data["Indicator Name"].unique()


# In[21]:


# Fields of interest
fac = ['Population, total', 'Forest area (% of land area)', 'Forest area (sq. km)', 'Arable land (% of land area)',
       'Agricultural land (% of land area)', 'Agricultural land (sq. km)']

data = data[data["Indicator Name"].isin(fac)]


# In[22]:


# Extracting valid countries
import pycountry
countries = [i.name for i in pycountry.countries]
data = data[data["Country Name"].isin(countries)]


# In[38]:


import matplotlib.pyplot as plt
data.groupby("Country Name").sum().sort_values("2020", ascending=False).iloc[:16, :].mean(axis=1).plot(kind="bar", figsize=(15, 6))
plt.ylabel("Area")
plt.title("Top 15 Countries with all Area")
plt.show()