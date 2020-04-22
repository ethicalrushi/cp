t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().strip().split()]
    a = str(bin(a))[2:]
    b = str(bin(b))[2:]

    if len(a)>len(b):
        b = '0'*(len(a)-len(b))+b
    else:
        a = '0'*(len(b)-len(a))+a
    
    mx = int(a,2)^int(b,2)
    res = 0
    n = len(a)
    j = 1
    while j<n:
        nb= b[-1]+b[0:-1]
        if int(nb,2)^int(a,2)>mx:
            mx = int(nb,2)^int(a,2)
            res=j
        elif int(nb,2)^int(a,2)==mx:
            if j<res:
                res=j
        else:
            pass

        b = nb
        j+=1
    print(res, mx)


