from bisect import bisect_left
 
def solve(arr, myNumber):
    pos = bisect_left(arr, myNumber)
    if pos == 0:
        return arr[0]
    if pos == len(arr):
        return arr[-1]
    before = arr[pos - 1]
    after = arr[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    res = 10**20
    a.sort()
    c.sort()
    b.sort()
    for x in a:
        y=solve(b,x)
        z=solve(c,x)
        res = min(res,((x-y)**2+(y-z)**2+(z-x)**2))
    for x in b:
        y=solve(a,x)
        z=solve(c,x)
        res = min(res,((x-y)**2+(y-z)**2+(z-x)**2))
    for x in c:
        y=solve(b,x)
        z=solve(a,x)
        res = min(res,((x-y)**2+(y-z)**2+(z-x)**2))
    
    print(res)