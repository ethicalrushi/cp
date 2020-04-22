n, k = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

dp = [[0 for j in range(k+1)] for i in range(n+1)]
mod = 10**9+7

# def solve(i,k):
#     # print(i,k)
#     if i==n and k==0:
#         return 1
    
#     if i==n:
#         return 0

#     if k<0:
#         return -1

#     # print(i,k,a[i])
#     if dp[i][k] is not None:
#         return dp[i][k]%mod

#     dp[i][k] = 0
#     temp = 0
#     for j in range(min(k,a[i])+1):
#         if temp==1:
#             dp[i][k] = (dp[i][k]%mod + 1)%mod
#         else:
#             temp = solve(i+1,k-j)
#             dp[i][k] = (dp[i][k]%mod + temp%mod)%mod
    
#     return dp[i][k]%mod

dp[n][0] = 1
for i in range(n-1,-1,-1):
    for j in range(0,a[i]+1):
        dp[i][j] += dp[i+1][k-j]
# print(solve(0,k))
print(dp)