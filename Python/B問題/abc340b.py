q = int(input())
answer = []
ans = []
anspend = ans.append
append = answer.append
for s in range(q):
    num,num2 = map(int,input().split())
    if num == 1:
        append(num2)
    else:
        anspend(answer[-1*num2])
for i in range(len(ans)):
    print(ans[i])