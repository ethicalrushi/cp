t= int(input())
for _ in range(t):
    n, m = [int(x) for x in input().strip().split()]

    i = n
    j = m

    if i%j==0:
        print("YES")
    else:
        print("NO")