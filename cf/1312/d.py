def ncr(n, r, p): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  
            p - 2, p)) % p 


mod = 998244353

n, m = [int(x) for x in input().strip().split()]

res = 0
ans = 0
for i in range(n-1,1,-1):
    res = ncr(m,i,mod)
    res = (res%mod * (i-1)%mod * (n-i)%mod)%mod
    ans = (ans%mod +res%mod)%mod

print(ans)
