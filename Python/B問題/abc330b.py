n,l,r = map(int,input().split())
a = [int(i) for i in input().split()]
ans = [0]*n

for i in range(n):
    s = a[i]
    if s >= r:
        ans[i] = r
    elif a[i] <= l:
        ans[i] = l
    else:
        ans[i] = s
print(*ans)
