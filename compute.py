#!/usr/bin/env python
# coding: utf-8

# In[2]:


def mean(*n):
    sum=0
    counter=0
    for x in n:
        counter=counter+1
        sum+=x
    mean=sum/counter
    return mean
mean(45,65,87)







# In[5]:


def median(*n):
    list1=list(n)
    list1.sort()
    l=len(list1)
    if l%2==0:
        med=(list1[int (l/2)]+list1[int((l/2))-1])/2
    else:
        med=list1[int(l/2)]
    return med


median(23,54,87,69)






# In[ ]:





# In[ ]:




