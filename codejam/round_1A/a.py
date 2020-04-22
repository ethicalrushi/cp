t = int(input())
for _ in range(t):
    n = int(input())

    if n==501:
        res = [(1,1),(2,1),(3,2)]
        for i in range(4,501):
            res.append((2,1))
    else:
        res = [(1,1) for i in range(n)]

    print("Case #{}:".format(_+1))
    for r in res:
        print(r[0], r[1])