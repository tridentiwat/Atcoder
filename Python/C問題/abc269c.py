import numpy as np
import itertools
n = np.array([int(x) for x in format(int(input()),"b")])
a = np.array(list(reversed(n)))
one = np.where(a==1)[0]
two = []
result = []
for x in range(1,len(one)+1):
	for y in itertools.combinations(one, x):
		two.append(list(y))
for x in two:
	m = 0
	for y in range(len(x)):
		m = m + pow(2,x[y])
	result.append(m)
print(0)
for x in sorted(result):
	print(x)