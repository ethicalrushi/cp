t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().strip().split()]
    mat = [[None for j in range(m)] for i in range(n)]
    t=0
    for i in range(n):
        t=i%2
        for j in range(m):
            if t==0:
                mat[i][j]='B'
                t=1
            else:
                mat[i][j]='W'
                t=0

    if (n*m)%2==0:
        if mat[0][-1]=='W':
            mat[0][-1]='B'
        elif mat[-1][0]=='W':
            mat[-1][0]='B'
        elif mat[-1][-1]=='W':
            mat[-1][-1]='B'
        else:
            pass

    for i in range(n):
        res= "".join(m for m in mat[i])
        print(res)
    