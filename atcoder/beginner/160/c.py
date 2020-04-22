k, n = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

diff = []
res = abs(a[0]-a[1])
ld = abs(k-a[-1])+abs(a[0]-0)
for i in range(1,n):
    res = max(res,abs(a[i-1]-a[i]))

res = max(res, ld)
res = k-res
print(res)



