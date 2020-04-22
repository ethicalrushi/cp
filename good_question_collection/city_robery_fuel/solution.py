import bisect

n, x, k = [int(x) for x in input().strip().split()]
arr = []
for i in range(n):
    temp = [int(x) for x in input().strip().split()]
    arr.append(temp)

arr.sort()

ind = bisect.bisect_right(arr,x)

res = 0
init = x
i=ind
fuel = k
while i<n and fuel>0:
    diff = arr[i][0]-x
    fuel-=diff
    if fuel>=0:
        res+=arr[i][1]
    else:
        fuel+=diff
    i+=1

if fuel

