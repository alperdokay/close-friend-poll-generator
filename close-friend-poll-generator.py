#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import time


# In[32]:


items = ['Baklava', 'Şöbiyet', 'Ekmek Kadayıfı', 'Sütlaç', 'Şekerpare', 'Kemalpaşa', 'Künefe', 'Katmer']
ordered_elements = []
while len(items) != 0:
    num = random.randint(0, len(items) - 1)
    pick = items[num]
    del items[num]
    ordered_elements.append(pick)


# In[36]:


# Final Presentation
i = 1
prev_elem = None
for elem in ordered_elements:
    print("%d. element seçiliyor..." % i)
    for j in range(1):
        print(".")
        time.sleep(3)
    print(elem)
    if (i % 2 == 0):
        print("-------------------------------")
        print("%d. anket" % (i/2))
        print(prev_elem + " vs " + elem)
        print("-------------------------------")
    prev_elem = elem
    i += 1
    time.sleep(1)
    
    


# In[ ]:




