n = int(input())
a = [int(x) for x in input().strip().split()]
dic = {}

s=0
dic = {}
dic[0] = [0,[10**10,]]
for i in range(n):
    s+=a[i]
    if s not in dic:
        dic[s] = [0,[]]
    dic[s][1].append(i)

if len(dic[0][1])>1:
    dic[0][0]=1

i=1
s=a[0]
res=0
while i<n:
    s+=a[i]
    si = i
    dic[s][0]+=1
    if dic[s][0]>=len(dic[s][1]):
        ei = n-1
    else:
        ei = dic[s][1][dic[s][0]]-1
    res+=(ei-si+1)
    # print(si, ei, s)
    i+=1

s=a[0]
si=0
dic[s][0]=1
if dic[s][0]>=len(dic[s][1]):
    ei = n-1
else:
    ei = dic[s][1][dic[s][0]]-1

if len(dic[0][1])>1:
    dic[0][0]=1
else:
    dic[0][0]=0
print(dic)

zind = dic[0][1][dic[0][0]]-1
ei = min(ei, zind)
res+=(ei-si+1)
# print(si, ei, s)

print(res)