s = input()
u = s.rfind('|')
m = s.find('|')
print(s[:m]+s[u+1:])