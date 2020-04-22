def next_mx(arr, n): 
    mx = -1
    ans =[[None,None] for i in range(n)]
    ans[-1] = -1
    ind = n
    for j in range(n-2,-1,-1):
        if mx<arr[j+1]:
            mx = arr[j+1]
            ind = j+1

        # mx = max(mx, arr[j+1])

        ans[j] = [mx,ind]
    
    return ans




n, m = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

mx = next_mx(a,m)
print(mx)
res = []
ind = 0
flag=True

for i in range(m):
    if i+a[i]>n:
        flag=False
        break

if sum(a)<n:
    flag=False
else:
    if flag:
        ind =0
        res.append(1)
        
        for i in range(m-1):
            pi = max(mx[i][0], m-mx[i][1])
            li = n-pi

            # print(li)
            # print(ind+a[i]+mx[i][1]-i-1)
            if ind+a[i]+mx[i][1]-i-1<li:
                # print("a")
                # pi = 
                ind = ind+a[i] #give all

            else:
                # print("b", ind)
                # print(li, mx[i][1], i)
                # print(ind+a[i], li-(mx[i][1]-i-1))
                ind = li-(mx[i][1]-i-1)
                # ind = min(ind+a[i], li-(mx[i][1]-ind-1))
                
            # print(ind)
            res.append(ind+1)

if flag:
    print(*res)
else:
    print(-1)








