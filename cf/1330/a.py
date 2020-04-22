t = int(input())
for _ in range(t):
    n, x = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    a = set(a)

    j=1
    k=0
    while k<=x:
        if j in a:
            j+=1
        else:
            k+=1
            j+=1
        # print(x,j)
    print(j-2)