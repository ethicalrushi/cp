n, m, k = [int(x) for x in input().strip().split()]

arr = []
for _ in range(k):
    x, y = [int(x) for x in input().strip().split()]
    arr.append((x,y))

diff = [] 

targ = []

for i in range(k):
    x, y = [int(u) for u in input().strip().split()]
    # targ.append((x,y))
    x0, y0 = arr[i]
    x1 = x-x0
    y1 = y-y0
    # diff.append([x1, y1, (x,y)])
    tdiff = [0,0,0,0]
    if x1<0:
        tdiff[0] = -1*x1
    else:
        tdiff[1] = x1

    if y1<0:
        tdiff[2] = -1*y1
    else:
        tdiff[3] = y1 
    diff.append([tdiff,(x,y),[x0,y0]])
# print(diff)
xg, yg = 0,0
diff.sort()
res = ''

# print(diff)
for i in range(k):
    
    if diff[i][0][0]==0:
        x1 = diff[i][0][1]
    else:
        x1 = -1*diff[i][0][0]

    if diff[i][0][2]==0:
        y1 = diff[i][0][3]
    else:
        y1 = -1*diff[i][0][2]
    # print('x1',x1, 'y1', y1)
    # nx1=x1-xg
    # # ny1=y1-yg
    # print(diff[i][0],'x1',x1, 'y1', y1)

    if x1<0:
        res+='U'*(-1*x1)
    else:
        res+='D'*x1
    
    if y1<0:
        res+='L'*(-1*y1)
    else:
        res+='R'*y1
    # print(res)
    for j in range(i+1, k):
        targ = diff[j][1]
        aj = diff[j][2]
        # print('##',diff[j][0], aj, targ)
        xog = aj[0]+x1
        if xog<1:
            xog=1
        if xog>n:
            xog=n
        yog = aj[1]+y1
        if yog<1:
            yog=1
        if yog>m:
            yog=m
        aj = [xog, yog]
        tx, ty = targ
        xd = tx-xog
        yd = ty-yog
        tdiff = [0,0,0,0]
        if xd<0:
            tdiff[0] = -1*xd
        else:
            tdiff[1] = xd

        if yd<0:
            tdiff[2] = -1*yd
        else:
            tdiff[3] = yd 
            
        diff[j] = [tdiff,targ,aj]
        # print('****',arr[j], targ, diff[j][0])
    # print(diff)



    # xg += nx1
    # yg += ny1
    # print(res)
    # print('xg',xg, 'yg', yg)

if len(res)<=2*m*n:
    print(len(res))
    print(res)
else:
    print(-1)





    