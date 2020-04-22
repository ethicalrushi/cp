#19:00
n, wm = [int(x) for x in input().strip().split()]
w = []
v = []
for i in range(n):
    wi, vi = [int(x) for x in input().strip().split()]
    w.append(wi)
    v.append(vi)

dp = [[None for i in range(wm+1)] for j in range(n)]

def solve(i,j):
    if dp[i][j]:
        return dp[i][j]
    if i<0:
        return 0
    else:
        if j>=w[i]:
            dp[i][j] = max(solve(i-1,j), solve(i-1,j-w[i])+v[i])
        else:
            dp[i][j] = solve(i-1,j)

    return dp[i][j]

print(solve(n-1,wm))
# print(dp)