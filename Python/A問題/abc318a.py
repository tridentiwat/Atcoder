n,m,p = map(int,input().split())
cnt = 0
fullmoon = m
while n >= fullmoon:
    cnt += 1
    fullmoon = m + cnt * p
print(cnt)