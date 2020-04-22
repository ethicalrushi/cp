"""
Important Note; l_dp.py looks very similar to this, but that soln is
incorrect because the way recursion is written
The term d which is used for output is passed as an argument,
hence it becomes a state in dp, which is not handled.

General tip: Avoid passing result as parameter in recursive funcns for dp
"""

n = int(input())
a = [int(x) for x in input().strip().split()]
dp = [[[None for k in range(2)] for j in range(n)] for i in range(n)]

def solve(a,i,j,t):
    if dp[i][j][t]:
        return dp[i][j][t]

    elif i==j:
        if t==1:
            d=1
        else:
            d=-1
        dp[i][j][t]= d*a[i]

    elif t==1:
        dp[i][j][t]= max(solve(a,i+1,j,0)+a[i], solve(a,i,j-1,0)+a[j])

    else:
        dp[i][j][t]= min(solve(a,i+1,j,1)-a[i], solve(a,i,j-1,1)-a[j])

    return dp[i][j][t]

print(solve(a,0,n-1,1))