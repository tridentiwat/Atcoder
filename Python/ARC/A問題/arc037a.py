n = int(input())
a = [int(x) for x in input().split()]
study = 0
for i in range(n):
    if a[i] < 80:
        study = study + 80 - a[i]
print(study)