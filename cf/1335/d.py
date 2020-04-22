t = int(input())

for _ in range(t):
    a = []
    for i in range(9):
        s = [int(x) for x in input()]
        a.append(s)
    
    c=0
    i=0
    j=0
    initj=0
    while c!=9:
        if (i+1)%3!=0:
            # print((i,j), (i+1,j))
            a[i][j] = a[i+1][j]
            i+=1
            j+=3
        else:
            # print((i,j),(i-1,j))
            a[i][j] = a[i-1][j]
            initj+=1
            j=initj
            i+=1
        c+=1
    

    for i in range(9):
        rs = "".join(str(x) for x in a[i])
        print(rs)
