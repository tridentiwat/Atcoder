import numpy as np
n,m = map(int,input().split())
a = np.array([int(x) for x in input().split()])
x = np.array([0]*m)
for i in range(n):
    x = x + [int(x) for x in input().split()]
if np.all(a<=x):
    print("Yes")
else:
    print("No")