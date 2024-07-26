h = 21
m = 0
k = int(input())
if k >= 60:
    h += 1
    m = k%60
else:
    m = k
print(f"{h:02}:{m:02}")