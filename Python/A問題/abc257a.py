n,x = map(int,input().split())
c = 0
if x%n == 0:
    c = x//n
else:
    c = x//n + 1
print(chr(64+c))