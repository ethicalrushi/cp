n = int(input())
arr = [int(x) for x in input().strip().split()]
dp = [None for i in range(n)]
dp[0] = 0
dp[1] = abs(arr[1]-arr[0])
for i in range(2,n):
    dp[i] = min(dp[i-1]+abs(arr[i]-arr[i-1]),dp[i-2]+abs(arr[i]-arr[i-2]))
print(dp[n-1])