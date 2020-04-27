t = int(input())
mod = 10**9+7

def add(a,b,m):
    if((a+b)>=m):
        return (a+b)%m
    return a+b

def mul(a,b,m):
    if((a*b)<m):
        return a*b
    return (a*b)%m

 

for _ in range(t):
    n, k = [int(x) for x in input().strip().split()]
    res= pow(n,2,mod)%mod

    if(n==0):
        print(((k-1)*k)%mod)
    else:
        k-=1
        if k%2==0:
            a1 = k//2
        else:
            a1 = k//2+1
        a2 = k-a1

        k1 = mul(a1,2*n,mod)%mod
        k2 = add(a2,1,mod)%mod
        k2 = mul(k2,a2,mod)%mod
        res = add(k1,res, mod)%mod
        res = add(res, k2, mod)%mod

        print(res%mod)