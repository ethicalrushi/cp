t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]

    if max(a)==max(b):
        print("NO")
    else:
        print("YES")