n,q = map(int,input().split())
answer = []
player = {i:0 for i in range(1,n+1)}
for _ in range(q):
    a,b = map(int,input().split())
    if a == 1:
        player[b] += 1
    elif a == 2:
        player[b] += 2
    else:
        if player[b] >= 2:
            answer.append("Yes")
        else:
            answer.append("No")
print(*answer,sep="\n")