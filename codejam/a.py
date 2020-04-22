t = int(input())
for _ in range(t):
    n = int(input())
    mat = []

    for i in range(n):
        arr = [int(x) for x in input().strip().split()]
        mat.append(arr)
    
    trace=0
    for i in range(n):
        trace+=mat[i][i]
    
    row=0
    for i in range(n):
        rset = set(mat[i])
        if len(rset)<n:
            row+=1
    
    col=0
    for i in range(n):
        cset = set([])
        for j in range(n):
            if mat[j][i] not in cset:
                cset.add(mat[j][i])
            else:
                col+=1
                break
    res = "Case #{}: {} {} {}".format(_+1, trace, row, col)
    print(res)

