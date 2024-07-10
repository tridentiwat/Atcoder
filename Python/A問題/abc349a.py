import numpy as np
n = int(input())
a = np.array([int(i) for i in input().split()])
sm = np.sum(a)
print(sm*-1)
