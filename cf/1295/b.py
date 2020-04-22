t = int(input())
for _ in range(t):
    n, x = [int(x) for x in input().strip().split()]
    s = input()
    a = []
    for e in s:
        if e=='0':
            a.append(1)
        else:
            a.append(-1)

    dic = {}
    cs=0
    for e in a:
        cs+=e
        if cs not in dic:
            dic[cs]=0
        dic[cs]+=1

    bs = sum(a)
    nthres= dic[bs]
    print(dic)
    print(bs, x)
    print(a)
    res=0
    if bs==0:
        cs=0
        for elem in a:
            cs+=elem
            if cs==x:
                res=-1
                break
            
    else:
        #pos mod :
        if bs<0:
            if x<0:
                bs = -1*bs
                x = x*bs
                for e in a:
                    e = e*-1
            # else:

        else:
            nx = x%bs
            print(nx)
            cs=0
            for elem in a:
                cs+=elem
                if cs==nx:
                    res+=1

            
            #neg mod :
            cs = 0
            x = x- bs*(x//bs+1)
            for elem in a:
                cs+=elem
                if cs==x:
                    res+=1
            
            if nx==0 and bs>0:
                res+=nthres

    print(res)

            
        


