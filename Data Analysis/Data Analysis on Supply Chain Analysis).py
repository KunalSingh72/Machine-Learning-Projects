#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


df = pd.read_csv("supply_chain.csv")
df


# In[6]:


df.head()


# In[7]:


import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"


# In[8]:


df.describe()


# # Now let's get started with analyzing the supply chain by looking at the relationship between the price of the products and the revenue generated by them:

# In[9]:


fig = px.scatter(df, x ='Price',
                y = 'Revenue generated',
                color = 'Product type',
                hover_data = ['Number of products sold'],
                trendline = 'ols')
fig.show()


# In[10]:


sales_data = df.groupby('Product type')['Number of products sold'].sum().reset_index()

sales_data


# In[11]:


pie_chart = px.pie(sales_data, values = 'Number of products sold', names='Product type',
                  title='Sales by Product Type',
                  hover_data = ['Number of products sold'],
                  hole = 0.5,
                  color_discrete_sequence = px.colors.qualitative.Pastel)
pie_chart


# In[12]:


pie_chart.update_traces(textposition = 'inside', textinfo = 'percent+label')
pie_chart.show()


# # So 45% of gthe nusiness comes from skincare products, 29.5%from haircare, and 25.5%from cosmetics. Now let's have a look at the total revnuie generated from shipping carrirers:

# In[13]:


total_revenue = df.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()
total_revenue


# In[14]:


fig = go.Figure() # GO : graphical objects
fig.add_trace(go.Bar(x = total_revenue['Shipping carriers'],
                     y = total_revenue['Revenue generated']))
fig.update_layout(title = 'Total Revenue by Shipping Carrier',
                 xaxis_title = 'Shipping Carrier',
                 yaxis_title = 'Revenue Gernerated')
fig.show()


# In[15]:


avg_lead_time = df.groupby ('Product type') ['Lead time'].mean().reset_index() 
# avg_lead_time
avg_manufacturing_costs = df.groupby('Product type') ['Manufacturing costs'].mean().reset_index()
result = pd.merge(avg_lead_time, avg_manufacturing_costs, on='Product type') 
result.rename(columns={'Lead time': 'Average Lead Time',
                       'Manufacturing costs': 'Average Manufacturing Costs'}, inplace = True)
print(result)


# ## Analyzing SKUS
# There's a column in the dataset as SKUs. You must have heard it for the very first time. So, SKU stands for Stock Keeping
# Units. They're like special codes that help companies keep track of all the different things they have for sale. Imagine you have
# a large toy store with lots of toys. Each toy is different and has its name and price, but when you want to know how many you
# have left, you need a way to identify them. So you give each toy a unique code, like a secret number only the store knows.
# This secret number is called SKU.
# I hope you have now understood what's SKU. Now let's analyze the revenue generated by each SKU

# In[16]:


revenue_chart = px.line(df, x='SKU',
                       y='Revenue generated',
                       title='Revenue Generated by SKU')
revenue_chart.show()


# ## Ther's another column in the dataset as Stock levels. Stock levels refer to the number of products a stire or business has in its inventory. Now let's have a look at the stock levels of each SKU: 

# In[17]:


stock_chart = px.line(df,x = 'SKU',
                     y = 'Stock levels',
                     title = 'Stock level by SKU')
stock_chart


# ## Now let's have a look at the order quantity of each SKU : 

# In[18]:


order_quantity_chart = px.bar(df, x='SKU',
                                y = 'Order quantities',
                                title='Order Quantity by SKU')
order_quantity_chart


# # cost analysis

# ### now let's analyze the shipping cost of carriers cost of carrirs

# In[19]:


shipping_cost_chart =px.bar(df, x='Shipping carriers',
                                y = 'Shipping costs',
                                title='Shipping costs by carriers')
shipping_cost_chart.show()


# ## In one of the above visualizations , we discovered that carrier B helps the company in more revenue. It is also the most costly carrier among the three.  NOw let's have a look at the costd distribution by transportation mode:

# In[20]:


transportation_chart = px.pie(df,
                             values = 'Costs',
                             names = 'Transportation modes',
                             title = 'Cost Distribution by Transportation Mode',
                             hole = 0.5,
                             color_discrete_sequence = px.colors.qualitative.Pastel)
transportation_chart.show()


# # so the company spends more on Road and rails modes of transportastion for the transportation of goods.

# ## Analyzing Defect Rate

# #### the defect rate in the supply chain refers to the percentage of produicts that have something wrong or are found broken after shipping. Legt's have a look at the average defect rate of all product types:

# In[21]:


defect_rates_by_product = df.groupby('Product type')['Defect rates'].mean().reset_index()
fig = px.bar(defect_rates_by_product, x = 'Product type', y = 'Defect rates', title = 'Average Defect Rates by Product Type')
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




