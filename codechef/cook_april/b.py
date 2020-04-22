t = int(input())
mod = 10**9+7
for _ in range(t):
    n, a = [int(x) for x in input().strip().split()]
    res = 0
    i=1
    ca = a
    while i<=n:
        cp = pow(ca,2*i-1, mod)
        res = (res%mod + cp%mod)%mod
        ca = ((ca%mod)*(cp%mod))%mod
        i+=1
    
    print(res%mod)

