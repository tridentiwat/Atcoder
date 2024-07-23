a,b = map(int,input().split())
c = a//b
if a%b==0:
    print(c)
else:
    print(c+1)