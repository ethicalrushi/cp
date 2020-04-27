t = int(input())

for _ in range(t):
    n, k= [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]

    b = [0 for i in range(n)]
    for i in range(1,n-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            b[i] = 1
    
    # print(b)
 
    curr = sum(b[:k])
    if b[k-1]==1:
        curr-=1
    res=curr
    ri = 0
    end  =k-1
    for i in range(1,n-k+1):
        if b[i]==1:
            curr-=1
        
        if b[end]==1:
            curr+=1
        
        if curr>res:
            res = curr
            ri = i
        end+=1
    print(res+1, ri+1)

