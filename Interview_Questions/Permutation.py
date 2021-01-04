#!/usr/bin/env python
# coding: utf-8

# # Interview'da (Microsoft, Adobe, Airbnb, Apple) çıkmış bir soru daha :
# # Seviye : Advanced
# ========================================
# 
# Problem :
# 
# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input:
# [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# Dikkat:bangbang:
# Bu soruyu çözerken herhangi bir modul/kütüphane import etmeden ve def/lambda fonksiyon tanımlamadan yapmalısınız.

# In[22]:


from itertools import permutations
print(*list(permutations([1,2,3])),sep='\n')


# In[21]:


def perm(a, k=0):
   if k == len(a): print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

perm([1,2,3])

