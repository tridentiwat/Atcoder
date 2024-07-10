n = list(input())
numbers = (int(i) for i in n)
flg = True
od = next(numbers)
for i in range(len(n)-1):
    nw = next(numbers)
    if od <= nw:
        flg = False
        break
    od = nw
if flg:
    print("Yes")
else:
    print("No")