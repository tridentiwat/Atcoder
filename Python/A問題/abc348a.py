import numpy as np
n = int(input())
ans = np.arange(1,n+1)
ans = np.where(ans%3==0,"x","o")
print("".join(ans))