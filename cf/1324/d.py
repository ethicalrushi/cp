import bisect
n = int(input())
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]

c = [a[i]-b[i] for i in range(n)]

c.sort()

res = 0
for i in range(n):
    e = c[i]
    if e<0:
        ind = bisect.bisect_left(c,-1*e+1)
    elif e==0:
        ind = bisect.bisect_left(c,1)
    else:
        ind = ind+1
    temp = n-ind
    res+=temp
    
print(res)



