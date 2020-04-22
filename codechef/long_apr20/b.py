t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    a.sort(reverse=True)
    mod = 10**9+7
    res=0
    for i in range(n):
        res = (res%mod+max(0,a[i]-i)%mod)%mod
    

    print(res%mod)
