plant = 0
takahashi = int(input())
days = 0
while plant <= takahashi:
    plant += 1<<days
    days += 1
print(days)