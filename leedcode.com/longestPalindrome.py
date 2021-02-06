'''
### longestPalindrome
https://leetcode.com/problems/longest-palindromic-substring/
    
This problem was recently asked by Twitter:
    
A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

    Example:
    Input: "banana"
    Output: "anana"
        
    Input: "million"
    Output: "illi"
        
'''

# Alternative
def longestPalindrome(s):
    list= [s[i:j] for i in range(len(s)) for j in range(len(s),i,-1)  if s[i:j]==s[i:j][::-1]]
    return sorted(list,key=len,reverse=True)[0]
  
text = "banana"
print(longestPalindrome(text))


# Alternative
def longestPalindrome(s):
    a = ""
    b = {}
    for i in s:
        a += i
        if a in s[::-1]:
            b[a] = len(a)
        elif a != a[::-1]:
            a = a[1:]
    return max(b.keys(), key= lambda k: b[k])

text = "banana"
print(longestPalindrome(text))