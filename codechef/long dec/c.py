t = int(input())
inf = 10**10
for _ in range(t):
    n = int(input())
    s = input()

    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = [inf,i]
        else:
            temp_d = i-d[s[i]][1]
            d[s[i]] = [min(d[s[i]][0],temp_d),i]
    
    mn = inf
    for e in d:
        mn = min(mn,d[e][0])
    
    if mn==inf:
        res=0
    else:
        res=n-mn
    print(res)