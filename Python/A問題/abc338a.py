s = input()
sone = ord(s[0])
stwo = s[1:]
flg = True
if sone > 90 or sone < 65:
    flg = False
for i in stwo:
    if ord(i) > 122 or ord(i) < 97:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")