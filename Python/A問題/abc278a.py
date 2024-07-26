from collections import deque
n,k = map(int,input().split())
q = deque([int(i) for i in input().split()])
for _ in range(k):
    q.popleft()
    q.append(0)
print(*q)