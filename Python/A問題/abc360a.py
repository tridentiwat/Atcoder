s = input()
flg = True
for i in s:
    if i == "R":
        break
    elif i == "M":
        flg = False
        break
print("Yes" if flg else "No")