# https://www.hackerrank.com/challenges/zipped/problem
# student, subject = map(int,input().split())
# student, subject =5,3
# s1=[89,90,78,93,80]
# s2=[90,91,85,88,86]
# s3=[91,92,83,89,90.5]

student, subject = map(int,input().split())
s=[map(float,input().split()) for _ in range(subject)]
print(s)
for i in zip(*s): print(sum(i)/subject)

"""
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
"""

