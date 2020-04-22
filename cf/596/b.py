t = int(input())
for _ in range(t):
    n,k,d = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    c= 0
    i=0
    dic ={}
    for i in range(d):
        if a[i] not in dic:
            c+=1
            dic[a[i]]=1
        else:
            dic[a[i]]+=1
    i=1
    res=c
    c_t=c
    while i<=n-d:
        dic[a[i-1]]-=1
        if dic[a[i-1]]==0:
            c_t-=1
        if a[i+d-1] not in dic or dic[a[i+d-1]]==0:
            c_t+=1
            dic[a[i+d-1]]=1
        else:
            dic[a[i+d-1]]+=1
        res = min(res,c_t)
        i+=1
        
    print(res)