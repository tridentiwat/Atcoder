a,b = map(int,input().split())
c = a-b
if c > 3 or c < -2:
    print("No")
else:
    print("Yes")