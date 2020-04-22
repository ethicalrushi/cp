t = int(input())

for _ in range(t):
    n = int(input())

    s = input()
    flag=False
    r1 = ''
    r2 = ''
    for e in s:
        if e=='1':
            u = 0
            v = 1
            if flag:
                u, v = v,u
                flag=True
            flag=True
        elif e=='0':
            u = 0
            v = 0
        elif e=='2' and flag is False:
            u = 1
            v = 1
            # flag = True
        else:
            u = 2
            v = 0

        r1 += str(u)
        r2+= str(v)

    print(r2)
    print(r1)