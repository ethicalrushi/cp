t = int(input())

for _ in range(t):
    s = int(input())

    curr = 1
    cs=0
    cs+=curr
    curr = 2
    while s>cs:
        cs+=curr
        if s%cs==0:
            res = s//cs
            break
        curr = curr*2

    


    print(res)