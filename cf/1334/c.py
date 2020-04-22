t = int(input())
for _ in range(t):
    n  = int(input())
    a =[]
    for i in range(n):
        u, v = [int(x) for x in input().strip().split()]
        a.append([u,v])

    if n==1:
        res=a[0]
    else:
        mn = 10**10
        si = None
        for i in range(1,n):
            if a[i][0]>a[i-1][1]:
                diff = a[i-1][1]
            else:
                diff = a[i][0]

            if diff<mn:
                mn = diff
                si = i

        if a[0][0]>a[-1][1]:
            diff = a[-1][1]
        else:
            diff = a[0][0]
            
        if diff<mn:
            mn = diff
            si = 0
        # print(si)
        if si is None:
            res = min(a[i][0] for i in range(n))
        else:
            # res=0
            res=a[si][0]
            ct=1
            prev_i=si
            i = si+1
            
            if i==n:
                i=0

            while ct<n:
                # print(i, prev_i, res)
                res+=max(0,a[i][0]-a[prev_i][1])
                prev_i = i
                i+=1
                if i==n:
                    i=0

                ct+=1
        
        print(res)