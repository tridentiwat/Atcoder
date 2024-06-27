import numpy as np
a = np.array(["ABC" + f"{x:03}" for x in range(1,350)])
n = input()
if n == "ABC316":
    print("No")
elif n in a:
    print("Yes")
else:
    print("No")