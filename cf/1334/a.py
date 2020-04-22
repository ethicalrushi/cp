t = int(input())
for _ in range(t):
    n =int(input())
    p=0
    c=0
    flag=True
    for i in range(n):
        pi, ci = [int(x) for x in input().strip().split()]
        if pi<p:
            flag=False
        elif ci<c:
            flag=False
        elif ci-c>pi-p:
            flag=False
        else:
            p = pi
            c = ci

    
    if flag:
        print("YES")
    else:
        print("NO")
