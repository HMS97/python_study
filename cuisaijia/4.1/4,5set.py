#!/usr/bin/env python
# coding: utf-8

# In[21]:


l1=[x for x in range(200) if x%2==0]
t1=set(l1)
t1


# In[22]:


l2=[x for x in range(200) if x%3==0]
t2=set(l2)
t2


# In[23]:


s1=t1 & t2
s2=t1 | t2
s3=t1 - t2
print(s1)
print(s2)
print(s3)


# In[ ]:




