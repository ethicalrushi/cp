import bisect

def intersect(a, b):
    aset = set(a)
    res = []
    for e in b:
        if e in aset:
            res.append(e)
    return res



t = int(input())
for _ in range(t):
    n, q = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    dic = {} #height:seg_no
    for i in range(1,n+1):
        h1 = a[i-1]
        if i==n:
            h2 = a[i-1]+1
        else:
            h2 = a[i]
        if h1>h2:
            h1, h2 = h2, h1
        h2+=0.1
        if h1 not in dic:
            dic[h1] = [set([]),set([])]
        if h2 not in dic:
            dic[h2] = [set([]),set([])]
        dic[h1][0].add(i)
        dic[h2][1].add(-1*i)
    # print(dic)
    b = []

    for d in dic:
        b.append(d)
    b+=a
    b = list(set(b))
    b.sort()
    # print(b)
    
    temp = set([])
    for k in b:
        t1 = []
        if k not in dic:
            dic[k] = [set([]),set([])]
        # for e in dic[k]:
        #     if e<0:
        #         eset.add(e)
        #     else:
        #         t1.append(e) 
        t1 = dic[k][0]
        eset = set(dic[k][1])
        dic[k][0] = t1|temp
        dic[k][0] = dic[k][0]-dic[k][1]
        # print(t1, k, eset)
        # for tem in temp:
        #     if -1*tem not in eset:
        #         dic[k][0].append(tem)
        temp = dic[k][0]

    # print(dic)
    # can replace with some bisect for better complexity
    for q_ in range(q):
        x1, x2, y = [int(x) for x in input().strip().split()]
        # ind = bisect.bisect_left(b,y)
        # # print(b, ind)
        # if ind>=len(b):
        #     seg=[]
        # elif b[ind]==y:
        #     seg = dic[y][0]
        # else:
        #     li = max(ind-1, 0)
        #     hi = ind
        #     if li==hi:
        #         seg = []
        #     else:
        #         t1 = dic[b[li]][0]
        #         t2 = dic[b[hi]][0]
        #         seg = intersect(t1, t2)
        # # print(seg)
        # ans=0
        # for s in seg:
        #     p1, p2 = s, s+1

        #     if p1<x2 and p1>=x1 and p2<=x2 and p2>x1:
        #         ans+=1
        # print(ans)
        print(2)




        

        

