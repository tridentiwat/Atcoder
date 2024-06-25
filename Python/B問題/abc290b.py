import numpy as np
n,k = map(int,input().split())
s = np.array(list(input()))
tf = np.where(s=="o")[0]
for i in range(k,len(tf)):
    s[tf[i]] = "x"
print("".join(s))