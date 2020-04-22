t = int(input())

for _ in range(t):
    n, k= [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    dic = {}
    seg= [0 for i in range(2*k+5)]
    l = 0
    h = n-1
    while l<h:
        s= a[h]+a[l]
        if s not in dic:
            dic[s]=0
        dic[s]+=1

        mn = min(a[l],a[h])+1
        mx = max(a[l],a[h])+k
        seg[mn]+=1
        seg[mx+1]-=1
        l+=1
        h-=1

    

    tot = n//2

    s = 0
    for i in range(2*k+5):
        s+=seg[i]
        seg[i]=s

    res = n
    for i in range(2*k+5):
        curr = seg[i]
        if i in dic:
            onere=curr-dic[i]
            ca = dic[i]
        else:
            onere = curr
            ca = 0

        
        if ca>=tot:
            res=0
            break
        else:
            currres=onere
            if onere+ca>=tot:
                res = min(res,currres)
            else:
                rem = tot-ca-onere
                currres+=2*rem
                res = min(res, currres)
    
    print(res)