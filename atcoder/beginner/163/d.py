mod = 10**9+7
n,k = [int(x) for x in input().strip().split()]
res=0
for j in range(k,n+2):
    mn = (j-1)*j//2
    mx = j*(2*n-j+1)//2
    res = (res%mod+(mx-mn+1)%mod)%mod

print(res%mod)