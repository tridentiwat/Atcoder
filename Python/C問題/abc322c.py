import bisect
n,m = map(int,input().split())
a = [int(x) for x in input().split()]
for x in range(1,n+1):
    i = bisect.bisect_left(a, x)
    print(a[i]-x)