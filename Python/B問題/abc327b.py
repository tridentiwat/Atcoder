b = int(input())
ans = 0
for i in range(1,b+1):
    a = pow(i,i)
    if a >= b:
        ans = i
        break
if a == b:
    print(i)
else:
    print(-1)
