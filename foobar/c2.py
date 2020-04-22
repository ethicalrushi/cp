l = [int(x) for x in raw_input().strip().split()]
n = len(l)

dic = [0 for i in range(n)] #dic[i] contains indices of elements (j>i) such that arr[j] divisible by arr[i]


for i in range(n):
    dic[i] = []
    for j in range(i+1,n):
        if arr[j]%arr[i]==0:
            dic[i].append(j)

res = 0
for fe in dic:
    for se in dic[fe][0]:
        res+=dic[se][1]
print(res)


        
        
