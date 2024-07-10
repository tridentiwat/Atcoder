import numpy as np
n = int(input())
a = np.array([int(x) for x in input().split()])
b = np.array([int(x) for x in input().split()])
a2 = np.max(a)
b2 = np.min(b)
print(b2-a2+1 if b2-a2>=0 else 0)