n, m = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
flag=True

for i in range(m):
    if i+a[i]>n:
        flag=False
        break

if sum(a)<n:
    flag=False
else:
    res= [None for i in range(m)]
    ind = n
    for j in range(m-1, -1, -1):
        # print(j-1, ind-a[j])
        if ind-a[j]>j:
            ind-=a[j]
        else:
            ind = j
            # print('e',ind, n-a[j])
            if n-a[j]<ind:
                flag=False
                break
            
        # ind = max(0,j-1,ind-a[j])
        res[j] = ind+1
        



if flag:
    print(*res)
else:
    print(-1)








