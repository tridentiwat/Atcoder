s = input()
t = input()
slen = len(s)
ts = t[:slen]
if ts == s:
    print("Yes")
else:
    print("No")