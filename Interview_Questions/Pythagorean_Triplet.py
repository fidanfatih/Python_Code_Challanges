#!/usr/bin/env python
# coding: utf-8

# ### Pythagorean Triplet in an array
# https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
# 
# This problem was recently asked by Uber:
# 
# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a² + b² = c²
# 
#     Example:
#     Input: [3, 5, 12, 5, 13]
#     Output: True

# In[20]:


def triplet(nums):
    from itertools import permutations as p
    square= [i**2 for i in nums]
    per= list(p(square,3))
    for i in range(len(per)):
        if per[i][0]+per[i][1] == per[i][2]:
            return True
    else:
        return False

nums=[3, 5, 12, 5, 13]
triplet(nums)


# In[ ]:


# Alternate
a = [3, 5, 12, 5, 13, 4]
a = list(set(a))
a.sort()
pythagoreans = []
for i in range(len(a)):
    for j in a[i+1:]:
        x = a[i]
        y = j
        z = (x**2 + y**2)**0.5
        if z in a[i+2:]:
            pythagoreans += ([x,y,int(z)],)
print(pythagoreans)


# In[21]:


# Alternate
nums = [3, 5, 12, 5, 13]
print(*{True for i in a for j in a if i**2 + j**2 in [k**2 for k in a]})


# In[ ]:




