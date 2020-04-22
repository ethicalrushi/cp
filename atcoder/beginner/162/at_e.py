n, k = [int(x) for x in input().strip().split()]

dic = {}
mod = 10**9+7

for i in range(1,k+1):
    dic[i] = 0


for i in range(1,k+1):
    for j in range(i,k+1,i):
        dic[i]+=1

print(dic)

res=0
for i in range(1,k+1):
    l = dic[i]
    num = l**n-(l-1)**n
    # num = (n%mod * pow(n-1,l,mod))%mod
    res = (res%mod+(i%mod)*(num%mod))%mod
    # print(i, res)

# res = (res%mod+2)%mod
print(res%mod)
