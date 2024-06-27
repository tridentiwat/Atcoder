s = input()
t = input()
cnt = 0
ans = []
for i in range(1,len(t)+1):
    if s[cnt] == t[i-1]:
        cnt += 1
        ans.append(i)
print(*ans)
