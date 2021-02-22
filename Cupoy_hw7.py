
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


array1 = np.array([[10, 8], [3, 5]])


# 
# $ 1.運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣? $
# 

# In[7]:


array2 = np.linalg.inv(array1)

array2


# In[10]:


array3 = array1@array2

array3


# $對角元素為1，為單位矩陣$

# $ 2. 運用上列array計算特徵值、特徵向量?$

# In[11]:


w, v = np.linalg.eig(array3)


# In[12]:


#eigenvalue特徵值
w


# In[13]:


#eigenector特徵向量
v


# $3.運用上列array計算SVD? $

# In[14]:


SVD = np.linalg.matrix_rank(array3)

SVD

