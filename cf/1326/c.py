n, k = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]
mod = 998244353
a = []
i=0
for ar in arr:
    a.append((ar,i))
    i+=1

a.sort(reverse=True)
res = 1
s=0
ind = []
for i in range(k):
    s+=a[i][0]
    ind.append(a[i][1])

ind.sort()
for i in range(1,k):
    diff = ind[i]-ind[i-1]
    res = ((res%mod)*(diff%mod))%mod


print(s, res%mod)


