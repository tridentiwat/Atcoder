n,k,x = map(int,input().split())
count = 1
a = []
for i in [int(x) for x in input().split()]:
    a.append(i)
    if count == k:
        a.append(x)
    count += 1
print(*a)