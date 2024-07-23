import numpy as np
nday,mujiT = map(int,input().split())
s = np.array([int(x) for x in list(input())])
logoT = 0
uselogoT = 0
usemujiT = 0
for i in s:
    if i == 0:
        mujiT = mujiT + usemujiT
        logoT = logoT + uselogoT
        uselogoT = 0
        usemujiT = 0
    elif i == 1:
        if mujiT != 0:
            usemujiT += 1
            mujiT -= 1
        elif logoT != 0:
            uselogoT += 1
            logoT -= 1
        else:
            uselogoT += 1
    else:
        if logoT != 0:
            uselogoT +=1
            logoT -= 1
        else:
            uselogoT += 1
print(logoT+uselogoT)