n = int(input())
x,y = 0,0
for i in range(n):
    xi,yi = map(int,input().split())
    x = x + xi
    y = y + yi
if x == y:
    print("Draw")
elif x > y:
    print("Takahashi")
else:
    print("Aoki")