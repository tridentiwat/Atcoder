import numpy as np
n= int(input())
a = []
b = []
for i in range(n):
    a.append([x for x in list(input())])
for i in range(n):
    b.append([x for x in list(input())])
a = np.array(a)
b = np.array(b)
for i in range(2):
    print(np.where(a!=b)[i][0]+1)

