n , x, y = [int(x) for x in input().strip().split()]

k1 = max(x,y)
k2 = min(x,y)
x = k2
y = k1

for k in range(1,n):
    if k>=(y-x):
        norm = max(0,y-k-1)+max(0,n-x-k)
    else:
        norm = n-k
    offset = x-k+1
    if offset>0:
        link = min(x-offset+1, n-y+1)
    else:
        end = y-(offset)+1
        link = min(x,max(0,n-end+1))

    link1 = min(max(k-2+1,0), y-x-1)

    res = norm+max(0,link)+link1
    print(norm, link, link1)
    print(res)