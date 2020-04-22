n = int(input())
vac = []
for i in range(n):
    arr =  [int(x) for x in input().strip().split()]
    vac.append(arr)
dp = [[None, None, None] for _ in range(n)]
dp[0] = vac[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])+vac[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2])+vac[i][1]
    dp[i][2] = max(dp[i-1][1], dp[i-1][0])+vac[i][2]

print(max(dp[n-1]))
