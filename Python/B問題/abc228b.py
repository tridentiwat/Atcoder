n,x = map(int,input().split())
a = [int(i) for i in input().split()]
aa = [0 for _ in range(n)]
people = 0
for i in range(n):
    if aa[x-1] == 0:
        aa[x-1] = 1
        x = a[x-1]
        people += 1
    else:
        break
print(people)