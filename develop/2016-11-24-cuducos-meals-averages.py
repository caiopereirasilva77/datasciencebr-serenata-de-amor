
# coding: utf-8

# # Calculate averages in meal expenses

# In[1]:

import numpy as np
import pandas as pd

dtype = {
    'document_id': np.str,
    'congressperson_id': np.str,
    'congressperson_document': np.str,
    'term_id': np.str,
    'cnpj_cpf': np.str,
    'reimbursement_numbers': np.str
}


# In[2]:

df = pd.read_csv('../data/2016-11-19-reimbursements.xz', parse_dates=[16], dtype=dtype)
df.shape


# Isolate expenses with meals only.

# In[3]:

meals = pd.DataFrame(df[df['subquota_description']=='Congressperson meal'])
meals.shape


# ## Calculate the average spent with each meal

# Calculate the total spent with meals.

# In[4]:

total = meals['total_net_value'].sum()
total


# And the average:

# In[5]:

average = total / len(meals)
average


# In[6]:

'Approx. R$ {0:.2f} per meal.'.format(average)


# ## Calculate how many distinct months (year/month pair) we're talking about

# Isolate _year_ and _month_ from `issue_date` to be able to calclulate a monthly average.

# In[7]:

meals['issue_date'] = pd.to_datetime(meals['issue_date'], errors='coerce')
meals['issue_year'] = meals['issue_date'].dt.year
meals['issue_month'] = meals['issue_date'].dt.month


# Group by year and month pairs.

# In[8]:

grouped = meals.groupby(['issue_year', 'issue_month'])


# Average number of meals per month:

# In[9]:

average = len(meals) / len(grouped)
average


# In[10]:

'Approx. {0:.0f} meals per month.'.format(average)

