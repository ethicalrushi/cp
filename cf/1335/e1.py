t = int(input())
l=27
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    dp = [[0,n-1,n-1] for i in range(l)]#c,si,ei

    for i in range(n):
        e = a[i]
        if dp[e][0]==0:
            dp[e][1] = i
        dp[e][0]+=1
        dp[e][2] = i

    res = 0 
    for i in range(l):
        if dp[i][0]>0:
            dic = {}
            ei = dp[i][2]
            si = dp[i][1]
            c = dp[i][0]
            dic[i]=0
            mx=0
            for j in range(si,ei+1):
                if a[j] not in dic:
                    dic[a[j]]=0
                dic[a[j]]+=1
                if a[j]!=i and dic[i]<=c//2:
                    curr = 2*dic[i]+dic[a[j]]
                    mx = max(curr,mx)
                else:
                    for d in dic:
                        if d!=i:
                            dic[d]=0
            res = max(res, mx)

            # print(i,si,ei,mx,res)
    
    for d in dp:
        res = max(res, d[0])

    print(res)
    

            




    

