def count(s):
    c=0
    for e in s:
        if e=='1':
            c+=1
    return c

t = int(input())
for _ in range(t):
    n, q  = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]
    
    e =0
    o = 0
    for e in a:
        el = count(bin(e))
        if el%2==0:
            e+=1
        else:
            o+=1
            
    for i in range(q):
        p = int(input())
        el = count(bin(p))
        if el%2==0:
            flag=True
        else:
            flag=False
        
        if flag:
            print(e,o)
        else:
            print(o,e)

