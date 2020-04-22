
import math
t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().strip().split()]

    a = [int(x) for x in input().strip().split()]

    a.sort()
    iset = set([])

    res=True
    pi = 0
    for i in range(n):
        pi=0
        while a[i]!=0:
            if a[i]%k==0:
                ci=pi
                while a[i]%k==0 and a[i]!=1:
                    a[i]=a[i]//k
                    ci+=1
                if a[i]==1:
                    ind = ci
                    a[i]=0
                else:
                    if a[i]%k==1:
                        a[i] = a[i]-1
                        ind =ci
                        pi = ci
                    else:
                        res=False
                        break
            elif a[i]==1:
                ind = 0
                a[i]=0
            elif a[i]%k==1:
                ind =0
                a[i]-=1
            else:
                res=False
                break

            if ind not in iset:
                iset.add(ind)
            else:
                res=False
                break


    if res:
        print("YES")
    else:
        print("NO")


