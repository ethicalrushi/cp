t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    a.sort()
    mid = n//2
    l = mid-1
    h = mid+1
    c=0
    res = []
    res.append(a[mid])
    turn=False
    while c!=n-1:
        if turn:
            res.append(a[h])
            h+=1
            turn = False
        else:
            res.append(a[l])
            l-=1
            turn = True
        c+=1

    print(*res)