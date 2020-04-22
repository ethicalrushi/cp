t = int(input())

for _ in range(t):
    a,b,c,d = [int(x) for x in input().strip().split()]
    x,y,x1,y1,x2,y2 = [int(x) for x in input().strip().split()]

    lflag = False
    vflag = False

    if x+b-a>=x1 and x+b-a<=x2:
        if x2-x>=1 or x-x1>=1: #atleast 1 space
            lflag=True

    if y+d-c>=y1 and y+d-c<=y2:
        if y2-y>=1 or y-y1>=1:
            vflag=True

    if a==0 and b==0:
        lflag=True
    
    if c==0 and d==0:
        vflag=True


    if lflag and vflag:
        print("Yes")
    else:
        print("No")

