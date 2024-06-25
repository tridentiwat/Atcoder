n,q = map(int,input().split())
takahashi = (1<<n)-1
cnt = 0
t = [int(i) for i in input().split()]
for i in range(q):
    takahashi = takahashi^(1<<t[i]-1)

while takahashi > 0:
    cnt += takahashi&1
    takahashi >>= 1
print(cnt)