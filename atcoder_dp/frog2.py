n, k =  [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]
dp = [None for i in range(n)]
dp[0] = 0

for i in range(1,n):
    li = max(0,i-k)
    dp[i] = dp[li]+abs(arr[i]-arr[li])
    for j in range(li,i):
        dp[i] = min(dp[i], dp[j]+abs(arr[i]-arr[j]))
        
print(dp[n-1])