t = int(input())
for _ in range(t):
    n = int(input())

    res = 0
    res+=n//2
    if(n%2)==0:
        ans = '1'*res
    else:
        ans = '7'+'1'*(res-1)
    print(ans)
