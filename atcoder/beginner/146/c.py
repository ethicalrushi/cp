
a,b,x = [int(x) for x in input().strip().split()]

flag = False
for i in range(10,0,-1):
    t = x
    c = b*i
    if t>=c:
        t-=c
        t = t//a
        if t>=10**(i-1):
            res =t
            if t>=10**i:
                res = 10**i-1
            flag=True
            break
    if flag:
        break

if flag:
    if res>=10**9:
        res = 10**9
    print(res)
else:
    print(0)
