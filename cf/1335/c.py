t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]

    dic = {}

    for e in a:
        if e not in dic:
            dic[e] = 0
        dic[e]+=1
    
    mx=0
    for d in dic:
        if dic[d]>mx:
            mx = dic[d]
            sm = d
    
    dis = len(dic)-1
    # print(dic, dis, mx)
    if dis>=mx:
        res = mx
    elif dis+1<=mx-1:
        res = dis+1
    else:
        res = dis
    print(res)
    