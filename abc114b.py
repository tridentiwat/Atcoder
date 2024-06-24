s = input()
abs = 999
for i in range(len(s)-2):
    a = 753-int(s[i:i+3])
    if a < 0:
        a = a * -1
    if abs > a:
        abs = a
print(abs)