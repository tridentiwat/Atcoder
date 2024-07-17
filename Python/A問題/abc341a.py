n = int(input())
ans = ""
for n in range(n*2+1):
    if n%2==0:
        ans = ans + "1"
    else:
        ans = ans + "0"
print(ans)