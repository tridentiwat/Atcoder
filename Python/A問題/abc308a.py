import numpy as np
s = np.array([int(x) for x in input().split()])
sorts = np.sort(s)
flg = True
if np.any(s!=sorts):
    flg = False
if np.any((s<100)|(s>675)):
    flg = False
if np.any(s%25!=0):
    flg = False
if flg:
    print("Yes")
else:
    print("No")