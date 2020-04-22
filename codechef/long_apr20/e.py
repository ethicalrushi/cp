t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = []
    for e in a:
        if e%4==0:
            b.append(2)
        elif e%2==0:
            b.append(1)
        else:
            b.append(0)

    s=0
    i=0
    res=0
    st=0
    # print(b)
    while i<n:
        # print(st,i,s,res)
        while i<n and s<2:
            s+=b[i]
            i+=1
            
        while st<i and s>=2:
            res+=n-i+1 #continous mixed series
            s-=b[st]
            st+=1
            

    #only odd series
    count = []
    i=0
    while i<n:
        c=0
        if a[i]%2==1:
            while i<n and a[i]%2==1:
                i+=1
                c+=1
            count.append(c)
        else:
            i+=1

    r1=0
    for c in count:
        r1+=(c*(c+1))//2
    
    res+=r1
    print(res)