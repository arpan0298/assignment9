#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


st.title('data visualization exercise')
df1 = pd.read_csv('data.csv',index_col=0)


# In[3]:


@st.cache
def load_data(nrows):
    data = pd.read_csv('data.csv',nrows=nrows)
    return data


# In[4]:


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df1.head())


# In[5]:


st.bar_chart(df1['points'])


# In[6]:


df2 = pd.DataFrame(df1[:200], columns = ['points','price'])
df2.hist()
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)


# In[7]:


st.line_chart(df2)


# In[8]:


hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h


# In[9]:


st.sidebar.header('Vis. App')


# In[10]:


df1['province'].value_counts().head(10).plot.bar()
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)


# In[12]:


option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# In[ ]:




