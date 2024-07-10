import numpy as np
s = np.array([int(x) for x in list(input())])
s = np.where((s%3==0) & (s!=0),np.where(s==6,9,6),s)
s = s[::-1]
print("".join(map(str, s.tolist())))