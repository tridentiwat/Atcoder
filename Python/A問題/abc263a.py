x = [int(x) for x in input().split()]
x = {i:x.count(i) for i in x}
if len(x) != 2:
    print("No")
else:
    t = list(x.values())[0]
    if t == 2 or t == 3:
        print("Yes")
    else:
        print("No")