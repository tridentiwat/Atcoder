import numpy as np
s = np.array(list(input()))
b = np.where(s=="B")[0]
r = np.where(s=="R")[0]
k = np.where(s=="K")[0]
if b[0]%2 != b[1]%2:
    if r[0] < k[0] and k[0] < r[1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")