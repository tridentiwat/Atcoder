import numpy as np
n,l,r = map(int,input().split())
a = np.arange(1,n+1)
b = a[l-1:r]
b =np.sort(b)[::-1]
a[l-1:r] = b
print(*a)