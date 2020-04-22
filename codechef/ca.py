t = int(input())

for _ in range(t):
    n,m,x,y = [int(x) for x in input().strip().split()]
    flag=False    

    if n==0 and m==0:
        flag=True
    if n==0 or x==0:
        if m%2==0 or y==0:
            flag=True
    elif m==0 or y==0:
        if n%2==0 or x==0:
            flag=True
    else:
        tot = n*x+m*y
        if tot%2==0:
            targ = tot//2
            for i in range(0,n+1):
                if i>=n+1:
                    break
                xs = i*x
                rem = targ-xs
                if rem%y==0:
                    rq = rem//y
                    if rq<=m:
                        flag=True
                        break

    if flag:
        print("YES")
    else:
        print("NO")
