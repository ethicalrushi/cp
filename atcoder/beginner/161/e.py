n, k, c= [int(x) for x in input().strip().split()]
s = input()

dp = [[None, None] for i in range(n)]

i=0
while i<n:
    if s[i]!='x':
        if i+c+1<n:
            dp[i][0] = i+c+1
        dp[i][1] = i
        i+=1
    else:
        ind =i
        while i<n and s[i]=='x':
            i+=1
 
        if i<n and s[i]!='x':
            for j in range(ind,i):
                dp[j][1] = i


print(dp)


