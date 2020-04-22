def left_below_diagonal(i,j):
    s = i-j
    temp = []
    for k in range(8,i,-1):
        # print(k, k-s)
        temp.append((k,k-s))

    return k, k-s, temp

def right_below_diagonal(i,j):
    s = j-i
    temp = []
    for k in range(8,j,-1):
        # print(k, k-s)
        temp.append((k-s, k))

    return k-s,k, temp

t = int(input())
for _ in range(t):
    res = []
    r, c = [int(x) for x in input().strip().split()]
    if r!=1 or c!=1:
        elem = (r+c)//2
        r, c= elem, elem
        res.append((r,c))
        res.append((1,1))
        # print(r,c)
        # print(1,1)

    r=1 
    c=1
    lr, lc = r, c
    while lr!=7:
        r, c, temp= left_below_diagonal(lr, lc) 
        res+=temp
        lr, lc = r+1, c-1
        res.append((lr,lc))
        # print(lr, lc)
    
    res.append((8,2))
    # print(2,8)
    res.append((4,6))
    res.append((1,3))
    # print(6,4)
    # print(3,1)
    r = 1
    c = 3
    lr, lc = r,c
    while lc!=7:
        r, c, temp= right_below_diagonal(lr,lc)
        res+=temp
        # break
        lr, lc = r-1, c+1
        res.append((lr,lc))
        # print(lr, lc)
    res.append((2,8))

    print(len(res))

    # res.sort()

    for r in res:
        print(*r)

    




    