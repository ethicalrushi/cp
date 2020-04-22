h , w = [int(x) for x in input().strip().split()]
mat = []
for _ in range(h):
    mat.append(input())

dp = [[0 for i in range(w)] for j in range(h)]
dp[0][0] = 1
mod = 10**9+7
for i in range(h):
    for j in range(w):
        if mat[i][j]=='#':
            dp[i][j] = 0
        elif i==0 and j==0:
            pass
        elif j<1 and i>=1:
            dp[i][j] = dp[i-1][j]%mod
        elif i<1 and j>=1:
            dp[i][j] = dp[i][j-1]%mod
        else:
            dp[i][j] = ((dp[i][j-1]%mod)+(dp[i-1][j]%mod))%mod

print(dp[h-1][w-1])
