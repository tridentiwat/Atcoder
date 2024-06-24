import numpy as np
from numba import jit
@jit(nopython=True)
def binary_search(x,a):
    left = 0
    right = len(a)
    while right >= left:
        mid = left+(right-left)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
    return right + 1

n,q = map(int,input().split())
a = np.array([int(x) for x in input().split()])
a = np.sort(a)
ans = np.zeros(q,dtype=int)
for i in range(q):
    ans[i] = binary_search(int(input()),a)
for i in range(q):
    prnt = n-ans[i]
    if prnt <= 0:
        print(0)
    else:
        print(prnt)

