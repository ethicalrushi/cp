t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    init = -10
    flag=True
    for i in range(n):
        if a[i]==1:
            diff = i-init
            if diff<6:
                flag=False
                break
            init = i

    if flag:
        print("YES")
    else:
        print("NO")
    
