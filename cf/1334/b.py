t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    a.sort(reverse=True)

    s=0
    res=0
    for i in range(n):
        s+=a[i]
        if s/(res+1)>=m:
            res+=1
        else:
            break
    
    print(res)
