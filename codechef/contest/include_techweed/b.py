n, k, m = [int(x) for x in input().strip().split()]
a =  [int(x) for x in input().strip().split()]

s = sum(a[:k])
flag = True
if s<m:
    flag = False

prev = 0
res = 0
i = k-1
out=False
while i<=n-k:
    print(s)
    if flag is False:
        cnt=1
        while i>0 and a[i]==0 and cnt<k:
            i-=1
            cnt+=1

        if cnt!=k and i==0:
            res=-1
            out = True
            break
        else:
            if i>=1:
                i-=1
            else:
                res=-1
                out = True
                break
            
        res+=1  #motivate all from i to i+k-1
        print(res, i)
        i = i+k
        j=1
        sj = 0
        print('#', i, j, k)
        while i<n and j<=k:
            sj+=a[i]
            i+=1
            j+=1
            # print(i,j,sj)
        
        if j<=k:
            out = True
            break
        else:
            s=sj
            i-=1
            print(s, i)
    else:
        i+=1
        s = s+a[i]-a[prev]
        prev+=1

    if out:
        break
  
    if s<=0:
        res = -1
        break
    elif s<m:
        flag = False
    else:
        flag = True

print(res)



    

