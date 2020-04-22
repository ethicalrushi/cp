t = int(input())
for _ in range(t):
    n = int(input())
    l = 1500
    seg = [0 for i in range(l)]
    activities = []
    for i in range(n):
        u, v = [int(x) for x in input().strip().split()]
        activities.append((u,v,i))
        seg[u]+=1
        seg[v]-=1
    

    flag=True
    for i in range(1,l):
        seg[i] += seg[i-1]
        if seg[i]>2:
            flag=False
            break
 
    if flag:
        seg = [1 for i in range(l)]
        activities.sort()
        ans = [None for i in range(n)]
        for activity in activities:
            st = activity[0]
            et = activity[1]
            if seg[st]%2==1:
                ans[activity[2]]='C'
                for k in range(st,et):
                    seg[k]=0
                seg[st]=0
                seg[et]=1
            else:
                ans[activity[2]]='J'
                seg[st]=1
                for k in range(st, et):
                    seg[k]=1
                seg[et]=2
            # print(st, et, seg[:12])
        
        ans = "".join(a for a in ans)

    else:
        ans = "IMPOSSIBLE"

    res = "Case #{}: {}".format(_+1, ans)
    print(res)