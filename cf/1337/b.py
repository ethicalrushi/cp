t = int(input())
for _ in range(t):
    x,n,m= [int(x) for x in input().strip().split()]

    if x>20:
        while n!=0:
            x=x//2+10
            n-=1
            if x<=20:
                break
    
    x-=m*10
    if x<=0:
        print("YES")
    else:
        print("NO")
    