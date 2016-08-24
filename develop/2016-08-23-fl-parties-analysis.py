
# coding: utf-8

# # Parties analysis

# * What parties have spent more money.
# * Find out if a congresspeople from the same party spend money on the same places.
# * Predict from what party a congressperson is from her expencies.

# In[1]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:

def read_csv(name):
    return pd.read_csv('../data/2016-08-08-%s.xz' % name,
                       parse_dates=[16],
                       dtype={'document_id': np.str,
                              'congressperson_id': np.str,
                              'congressperson_document': np.str,
                              'term_id': np.str,
                              'cnpj_cpf': np.str,
                              'reimbursement_number': np.str})


# In[3]:

last_year = read_csv('last-year')


# ## What parties have spent more money?
# 

# In[4]:

parties_sum = last_year.groupby('party', as_index=False).sum().sort_values('net_value', ascending=False)


# In[5]:

parties_sum.head()


# PMDB is the most expensive party.

# In[ ]:

sns.barplot(x='party',
            y='net_value',
            data=parties_sum)
locs, labels = plt.xticks()
plt.setp(labels, rotation=90); None


# ## Find out if a congresspeople from the same party spend money on the same places.
# 

# In[4]:

parties = last_year.groupby(['party', 'cnpj_cpf'], as_index=False).count()
parties = parties[['party', 'document_id', 'cnpj_cpf']].     sort_values(['party', 'document_id'], ascending=[True, False]).     drop_duplicates('party', keep='first')
parties.head()


# In[5]:

cnpj_list = pd.read_csv('../data/cnpj_info.xz')


# In[6]:

cnpj_list.iloc[0]


# In[7]:

cnpj_list['cnpj'] = cnpj_list['cnpj'].str.replace(r'[.\-/]', '')


# In[33]:

cnpj_list['atividade_principal'] = cnpj_list['atividade_principal'].str[33:-3]


# In[37]:

merged = pd.merge(parties, cnpj_list, how='left', left_on='cnpj_cpf', right_on='cnpj')
merged[['party', 'document_id', 'nome', 'atividade_principal']]


# In[ ]:



