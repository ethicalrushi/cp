t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    
    pi=n+1
    ni=n+1
    for i in range(n):
        if a[i]==1:
            pi=min(pi,i)
        
        if a[i]==-1:
            ni=min(ni,i)
    
    flag=True
    for i in range(n-1, -1,-1):
        # print(a[i], b[i], i, pi, ni)
        if a[i]<b[i]:
            if pi>=i:
                flag=False
                break
        elif a[i]>b[i]:
            if ni>=i:
                flag=False
                break
        else:
            pass
    
    if flag:
        print("YES")
    else:
        print("NO")