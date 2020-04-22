t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    i = 0
    res = 0
    while i<n:
        if a[i]>0:
            pi = 0 
            while i<n and a[i]>0:
                pi = max(pi, a[i])
                i+=1
                
            res+=pi
        else:
            ni = -10**10
            while i<n and a[i]<0:
                ni = max(ni,a[i])
                i+=1
            res+=ni
    print(res)