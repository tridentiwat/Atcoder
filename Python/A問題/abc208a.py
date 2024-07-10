a,b = map(int,input().split())
dice_max = 6*a
if b > dice_max or b < a:
    print("No")
else:
    print("Yes")