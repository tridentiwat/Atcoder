import numpy as np
n,k = map(int,input().split())
a = np.array([int(i) for i in input().split()])
a = np.where(a <= k,a,0)
a = np.unique(a)
m = np.sum(a)
ans = (k*(k+1))//2
print(ans - m)