n = int(input())

k = n//500
res=0
res+=k*1000

k = n%500
k = k//5

res+=k*5

print(res)