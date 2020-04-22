t = int(input())
for _ in range(t):
    arr = []
    q, stemp = [int(x) for x in input().strip().split()]
    for data in range(q):
        ti, l, h = [int(x) for x in input().strip().split()]
        arr.append((ti,l,h))

    arr.reverse()
    flag = True
    i=0
    l = arr[0][1]
    h = arr[0][2]
    while i<q-1:
        tdiff = arr[i][0]-arr[i+1][0]
        n_l = l-tdiff
        n_h = h+tdiff
        # print(n_l, n_h, arr[i+1][1], arr[i+1][2])
        if arr[i+1][2]<n_l or arr[i+1][1]>n_h:
            flag = False
            break
        else:
            l = max(n_l, arr[i+1][1])
            h = min(n_h, arr[i+1][2])
        i+=1
    
    l = l-arr[-1][0]
    h = h+arr[-1][0]
    if flag and stemp>=l and stemp<=h:
        print("YES")
    else:
        print("NO")
        


