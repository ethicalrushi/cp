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

    
    p = [(p[i],i+1) for i in range(d)]
    p.sort()
    s = [[None, None, None, None] for i in range(d)]

    m = len(ind)
    print(ind)
    if m==0:
        res=0
    else:
        for i in range(d):
            j = bisect.bisect_right(ind,p[i][0])
            print(p[i], j)
            if j==m:
                if ind[j-1]==p[i][0]:
                    s[i] = [p[i][1], p[i][1], None, None]
                else:
                    if abs(ind[j-1]-p[i][0])<=p[i][1]:
                        s[i][0]= p[i][1]-abs(ind[j-1]-p[i][0])
                    
            elif j==0:
                if abs(ind[0]-p[i][0])<=p[i][1]:
                    s[i][1] = p[i][1]-abs(ind[j-1]-p[i][0])
                
            else:
                prev = ind[j-1]
                nex = ind[j]
                print(prev, p[i][0])
                if prev==p[i][0]:
                    s[i] = [p[i][1], p[i][1], None, None]
                else:
                    if abs(prev-p[i][0])<=p[i][1]:
                        s[i][0] = p[i][1]-abs(prev-p[i][0])

                    if abs(nex-p[i][0])<=p[i][1]:
                        s[i][1] = p[i][1]-(abs(nex-p[i][0]))
            s[i][2] = p[i][1]
            s[i][3] = p[i][0]
            
        print(s)

        #merging
        arr = [] #right, left , day, pos
        j=0
        k=0
        while j<m or k<d:
            if j==m:
                arr.append(s[k])
                k+=1
            elif k==d:
                arr.append([0,0,0,ind[j]])
                j+=1
            else:
                if ind[j]<p[k][0]:
                    arr.append([0,0,0, ind[j]])
                    j+=1
                elif ind[j]==p[k][0]:
                    arr.append(s[k])
                    k+=1
                    j+=1
                else:
                    arr.append(s[k])
                    k+=1

        print(arr)


        def calc(i,j):
            r1,l1,d1,pos1 = i
            r2, l2, d2, pos2 = j
            fr = None
            fl = None
            ans =0
            if r1 is not None and r1>0:
                ir = pos1+r1
                fr = min(pos2-1, ir+d-d1)
            
            if r2 is not None and r2>0:
                il = pos2-l2
                fl = max(pos1,il-(d-d2))

            if fr and fl:
                if fl<=fr+1:
                    ans = pos2-pos1
                else:
                    ans = fr+1-pos1
                    ans+= pos2-fl
            elif fr:
                ans = fr+1-pos1
            elif fl:
                ans = pos2-fl
            else:
                ans=0

            return ans

        res = 0
        res = calc([0,0,0,0],arr[0])

        for i in range(1,len(arr)):
            res+= calc(arr[i-1],arr[i])
            print(res)
        
        print(res)

                








        




    
