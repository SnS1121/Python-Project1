#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv ('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv')


# In[7]:


df.describe()


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.shape


# In[27]:


df.info()


# In[33]:


df.isnull().sum()


# In[4]:


df.groupby(['School Level']).count()


# In[10]:


#isolating only specific columns
df[['School Level', 'School Name', 'Regents Exam', 'Year', 'Mean Score']]


# In[42]:


#created a new dataframe including only selected columns
df2 = df[['School Level', 'School Name', 'Regents Exam', 'Year', 'Mean Score', 'Total Tested']]


# In[56]:


#statistics on how many tested per School Level
df2.groupby(['School Level'])['Total Tested'].count()


# 

# In[46]:


import matplotlib.pyplot as plot
get_ipython().run_line_magic('matplotlib', 'inline')


# In[55]:


#plotting same columns, using bar chart; data shows that High School has the highest number of test taken out of all school levels.
df2.groupby(['School Level'])['Total Tested'].count().plot(kind='bar')


# In[59]:


#statistics on how many tested per Regents Exam
df2.groupby(['Regents Exam'])['Total Tested'].count()


# In[64]:


#plotted Regents Exam and Total Tested using Bar chart; data showed that Common Core Algebra had the highest number of test taken out of all of the Regent Exams.
df2.groupby(['Regents Exam'])['Total Tested'].count().plot(kind="bar")


# In[70]:


#focusing analysis only on Kings Collegiate Charter School
Kings_C= df2['School Name']== 'Kings Collegiate Charter School'
regents_exam = df2['Regents Exam']== 'Regents Exam'
total_tested= df2['Total Tested']== 'Total Tested'
year= df2['Year']== 'Year'


# In[72]:


df2_Kings_C= df2[Kings_C]


# In[73]:


df2_Kings_C.describe()


# In[75]:


#statistics on Kings Collegiate Charter School 
df2_Kings_C.groupby(['Regents Exam']).count()


# In[81]:


#statistics + plotted total tested by regents exam using bar chart; data showed Core Algebra also had the highest test taker.
df2_Kings_C.groupby(['Regents Exam'])['Total Tested'].count().plot(kind='bar')


# In[ ]:




