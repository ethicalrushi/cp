from math import log2, ceil
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    res = -1
    mx = a[0]
    for i in range(1,n):
        if a[i]>=mx:
            mx = a[i]
        else:
            d = mx-a[i]
            res = max(res,int(log2(d)))

    print(res+1)


    