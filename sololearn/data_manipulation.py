# https://www.sololearn.com/learning/eom-project/1093/111

import numpy as np
n, p = [int(x) for x in input().split()]

arr=[]

for i in range(n):
    arr+=[float(x) for x in input().split()]
print(np.array(arr).reshape(n,p).mean(axis=1).round(2))