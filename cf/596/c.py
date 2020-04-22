
import math
n, p = [int(x) for x in input().strip().split()]
given_n = n
if p==0:
    mx = int(math.log(n,2))+2
else:
    mx = n//abs(p)+1
dp = {}
# print(mx)
def solve(n,i,p):
    # print(n,i,p)
    if i >=mx:
        return 10**100
    if n<0:
        return 10**100
    if n==0:
        return 0
    if n in dp and dp[n][i]:
        return dp[n][i]

    if n not in dp:
        dp[n] = [None for i in range(mx)]
    if n-2**i-p==n:
        dp[n][i] = solve(n,i+1,p)
    else:
        dp[n][i] = min(solve(n-2**i-p,i,p)+1,solve(n,i+1,p))
    return dp[n][i]

if n+p<=0:
    print(-1)
else:
    ans= solve(n,0,p)
    if ans==10*100:
        ans=-1
    print(ans)