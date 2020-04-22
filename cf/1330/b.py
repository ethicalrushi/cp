t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    aset = set([])
    res = []
    s=0
    ts = sum(a)

    dic = {}
    #checking for invalid input with freq more tha  2
    for e in a:
        if e not in dic:
            dic[e]=0
        dic[e]+=1

    flag = True
    bad = set([])
    for d in dic:
        if dic[d]>2:
            flag=False
            break
        elif dic[d]==2:
            bad.add(d)

        


        

    if flag:
    
        for i in range(n-1):
            if a[i] not in aset:
                s+=a[i]
                aset.add(a[i])
                if a[i] in bad:
                    bad.remove(a[i])
                if ((i+1)*(i+2))//2==s:
                    # res.append(i+1)
                    ps = ts-s
                    rem = n-(i+1)
                    if ps==(rem*(rem+1))//2 and len(bad)==0:
                        res.append(i+1)
            else:
                break


        print(len(res))
        for r in res:
            print(r, n-r)
    else:
        print(0)



