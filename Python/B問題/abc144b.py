import numpy as np
s = input()
cnt = 0
answer = 0
acgt = np.array(["A","C","G","T"])

for i in s:
    if i in acgt:
        cnt += 1
        answer = max(answer,cnt)
    else:
        cnt = 0
print(answer)