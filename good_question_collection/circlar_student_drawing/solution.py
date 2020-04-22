n = int(input())
a = [int(x) for x in input().strip().split()]

dic = [0 for i in range(n+1)]
mx=0
res_id = 0

for i in range(n):
    if a[i]>i:
        diff = a[i]-i
        ei = n-diff
        if ei>i: #marking the segments
            si = i+1   
            dic[si]+=1
            dic[ei+1]-=1
    else:
        diff = i-a[i] #mark segments from 0-diff and i+1-n
        dic[0]+=1
        dic[diff+1]-=1
        if i!=n-1:
            dic[i+1]+=1
            dic[n]-=1

#sweep line algorithm
for i in range(1,n+1):
    dic[i]+=dic[i-1]

for i in range(n+1):
    if dic[i]>mx:
        mx = dic[i]
        res_id = i

print(res_id+1)