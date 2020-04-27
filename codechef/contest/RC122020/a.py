t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]

    dic = {}
    i=0
    for e in a:
        if e not in dic:
            dic[e] = [[i],1]
        else:
            if dic[e][0][-1]+1<i:
                dic[e][1]+=1
                dic[e][0].append(i)
        i+=1

    res=10**10
    mn = -1
    for d in dic:
        if dic[d][1]>mn:
            mn = dic[d][1]
            res=d
        if dic[d][1]==mn:
            res = min(res,d)

    print(res)
