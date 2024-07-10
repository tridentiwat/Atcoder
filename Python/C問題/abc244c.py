import numpy as np
n = int(input())
number = np.arange(1,2*n+2)
for i in range(n+1):
    takahashi = np.min(number)
    print(takahashi,flush=True)
    aoki = int(input())
    number = number[(number!=takahashi)&(number!=aoki)]
