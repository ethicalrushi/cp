t = int(input())

for _ in range(t):
    n =int(input())
    if n==1:
        res=0
    else:
        res= (n-1)-(n//2)
        # if n%2==0:
        #     res-=1
        if res<0:
            res=0
    print(res)