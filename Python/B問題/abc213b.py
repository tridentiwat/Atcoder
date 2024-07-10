import numpy as np
n = int(input())
s = [int(i) for i in input().split()]
s2 = np.sort(s)[::-1]
rank = np.where(s==s2[1])[0]
print(rank[0]+1)