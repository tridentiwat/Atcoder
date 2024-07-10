strings = "oxx"*6
s = input()
strings2 = strings.replace(s,"")
if strings2 == strings:
    print("No")
else:
    print("Yes")