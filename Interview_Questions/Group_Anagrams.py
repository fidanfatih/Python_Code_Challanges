#!/usr/bin/env python
# coding: utf-8

# In[127]:


'''
Facebook, Adobe ve Cisco gibi firmaların mülakatında çıkmış orta seviye bir Python sorusu :slightly_smiling_face:
=============================
Group Anagrams
Given a list of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''
def anagram(input):
    a = []
    for i in input:
        b = [j for j in input if "".join(sorted(i)) == "".join(sorted(j))]
        if sorted(b) not in a:
            a.append(sorted(b))
    return a

input=["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(input)


# In[129]:


def anagram(input):
    def uniq(input):
        items = []
        for i in input: 
            if i not in items: items.append(i)
        return items
    
    a,b=dict(),list()
    for i in input: a[i]=''.join(sorted(i))
    for j in uniq(a.values()): b.append(sorted([k for k,v in a.items() if v==j]))   
    return sorted(b,key=len,reverse=True)

input=["eat", "tea", "tan", "ate", "nat", "bat"]
anagram(input)


# In[130]:


def groupAnagrams(strs):
    anagrams = {}
    for i in strs:
        item = "".join(sorted(i))
        if item in anagrams:
            anagrams[item].append(i)
        else:
            anagrams[item]=[i]
    return anagrams.values()

groupAnagrams(input)


# In[134]:


def anagram(Input):
    output = []
    for i in Input:
        x = []
        for j in Input:
            if set(i) == set(j):
                x.append(j)
        if x not in output:
            output.append(x)
    return output

anagram(input)




