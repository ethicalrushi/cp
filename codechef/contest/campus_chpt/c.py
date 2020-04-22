import bisect
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    d = int(input())
    p = [int(x) for x in input().strip().split()]

    res = 0
    ind = []
    for i in range(n):
        if a[i]=='1':
            res+=1
            ind.append(i+1)

    
    p = [(p[i],i) for i in range(d)]
    p.sort()
    s = [False for i in range(2*d)]

    m = len(ind)
    if m==0:
        res=0
    else:
        for i in range(d):
            j = bisect.bisect_right(ind,p[i][0])
            if j==m:
                if abs(ind[j-1]-p[i][0])<=p[i][1]:
                    s[i]=True
            elif j==0:
                if abs(ind[0]-p[i][0])<=p[i][1]:
                    s[i]=True
            else:
                prev = ind[j-1]
                nex = ind[j]
                if abs(prev-p[i][0])<=p[i][1]:
                    s[i]=True
                if abs(nex-p[i][0])<=p[i][1]:
                    s[i]=True
        
        print(s)



        




    
