t,a,b = [int(x) for x in input().strip().split()]

for _ in range(t):
    u, v = -5,-5
    flag=False
    while u<=5:
        while v<=5:
            print(u,v)
            v+=1
            verd = input()
            if verd=='CENTER':
                flag=True
                break

        if flag:
            break
        u+=1
        v=-5






# res = "Case #{}: {} {} {}".format(_+1, trace, row, col)
# print(res)

