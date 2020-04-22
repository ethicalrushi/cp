dic = {}
n = int(input())
a = [int(x) for x in input().strip().split()]

for i in range(1,n+1):
    dic[i] =[]

for i in range(n-1):
    dic[a[i]].append(i+2)

res = [len(dic[i]) for i in range(1,n+1)]
for r in res:
    print(r)