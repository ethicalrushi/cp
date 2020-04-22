n = int(input())
a = []
for i in range(n):
    t = [int(x) for x in input().strip().split()]
    a.append(t)

mod = 10**9+7
dp = [0 for i in range(1<<n)]
dp[0] =1

def countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

def solve(m):
    if m>= 1<<n:
        return 0
    if dp[m]:
        return dp[m]
    for i in range(n):
        j = countSetBits(m)
        if (a[i][j]==1) and (m &(1<<i)==0):
            dp[m]+= solve(m|(1<<i))%mod


print(solve(0))

        
