month,day = map(int,input().split())
y,m,d = map(int,input().split())
if d == day:
    d = 1
    if m == month:
        m = 1
        y += 1
    else:
        m+= 1
else:
    d = d + 1
print(f"{y} {m} {d}")