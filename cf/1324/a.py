t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    c=0
    for e in a:
        if e%2==0:
            c+=1

    if c==0 or c==n:
        print("YES")
    else:
        print("NO")