n,d = map(int,input().split())
t = [int(x) for x in input().split()]
flg = False
for i in range(n-1):
    a,b = t[i],t[i+1]
    if b-a<=d:
        flg = True
        break
if flg:
    print(b)
else:
    print(-1)