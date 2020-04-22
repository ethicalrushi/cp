n,h,l,r = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

dp = [[None for i in range(h+1)] for j in range(n+1)]

def add(a,b):
    if a+b<=h:
        return a+b
    return (a+b)%h
def solve(i,t):
    # print(i,t)
    if i==n:
        return 0

    if dp[i][t] is not None:
        return dp[i][t]
    
    t1 = add(t,a[i]-1)
    t2 = add(t, a[i])

    if t1>=l and t1<=r:
        h1 = 1+solve(i+1,t1)
    else:
        h1 = solve(i+1, t1)

    if t2>=l and t2<=r:
        h2 = 1+solve(i+1,t2)
    else:
        h2 = solve(i+1, t2)
    
    dp[i][t] =  max(h1, h2)
    return dp[i][t]
    
print(solve(0,0))

    
    

