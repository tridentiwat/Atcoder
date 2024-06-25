import numpy as np
n = input()
building = np.array(list(map(int,input().split())))
t = np.where(building > building[0])[0]
print(t[0]+1 if len(t)!=0 else -1)