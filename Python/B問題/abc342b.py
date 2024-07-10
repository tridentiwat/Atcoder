n = int(input())
p = [int(i) for i in input().split()]
q = int(input())
ans = [0]*q
for i in range(q):
    a,b = map(int,input().split())
    aidx = p.index(a)
    bidx = p.index(b)
    mn = min(aidx,bidx)
    ans[i] = p[mn]
print(*ans,sep="\n")