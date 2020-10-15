# https://www.hackerrank.com/challenges/ginorts/problem
"""
You are given a string .
  string contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""
def sorting(s):
    if len(s)<1001 and s.isalnum():
        s,a=sorted(s),[]
        for j,c in enumerate(s):
            if not c.isdigit(): a=s[:j]+a;break
        a=list(filter(lambda x:int(x)%2,a))+\
          list(filter(lambda x:not int(x)%2,a))
        for i,c in enumerate(s):
            if c.islower(): a=s[j:i]+a;break
        return ''.join (s[i:]+a)
    else: return "invalid data"

print(sorting(input()))