t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    l = 0
    h = n-1
    comb = ''
    flag=False
    while s[l]==s[h] and l<=h:
        if l==h:
            temp = s[l]
            flag=True
            break
        comb+=s[l]
        l+=1
        h-=1

    rem = s[l:h+1]
    if len(rem)==0:
        temp1=''
    else:
        remh = {}
        i = 0
        for r in rem:
            if r not in remh:
                remh[r] = []
            remh[r].append(i)
            i+=1
        
        elem = remh[rem[0]][::-1]
        t1 = ''
        t2=''
        for e in elem:
            t = rem[0:e+1]
            if t==t[::-1]:
                t1=t
                break

        elem = remh[rem[-1]]
        for e in elem:
            t = rem[e:]
            if t==t[::-1]:
                t2=t
                break

        if len(t1)>len(t2):
            temp1 = t1
        else:
            temp1 = t2

    if flag:
        comb =comb+temp+comb[::-1]
    else:
        comb = comb+temp1+comb[::-1]

    print(comb)


    # dic = {}
    # i=0
    # for e in s:
    #     if e not in dic:
    #         dic[e] = []
    #     dic[e].append(i)
    #     i+=1


    # pre = ''
    # elem = dic[s[0]][::-1]
    # for e in elem:
    #     t = s[0:e+1]
    #     if t==t[::-1]:
    #         pre=t
    #         break

    # suff=''
    # elem = dic[s[-1]][::-1]
    # for e in elem:
    #     t = s[e:]
    #     if t==t[::-1]:
    #         suff=t
    #         break

    # p = len(comb)
    # q = len(pre)
    # r = len(suff)

    # print(comb, pre, suff)
    # if p==max(p,q,r):
    #     print(comb)
    # elif q==max(p,q,r):
    #     print(pre)
    # else:
    #     print(suff)


    
