n = int(input())
a = [int(x) for x in input().strip().split()]
dp = [[[None for k in range(2)] for j in range(n)] for i in range(n)]

def solve(a,i,j,t,d):
    if dp[i][j][t]:
        return dp[i][j][t]

    elif i==j:
        if t==1:
            d+=a[i]
        else:
            d-=a[i]
        dp[i][j][t]=d

    elif t==1:
        dp[i][j][t] = max(solve(a,i+1,j,0,d+a[i]), solve(a,i,j-1,0,d+a[j]))
    else:
        dp[i][j][t] = min(solve(a,i+1,j,1,d-a[i]), solve(a,i,j-1,1,d-a[j]))
    
    return dp[i][j][t]

print(solve(a,0,n-1,1,0))