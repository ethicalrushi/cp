t = int(input())

for _ in range(t):
    n = int(input())
    n = n//2
    if n%2==1:
        print("NO")
    else:
        print("YES")
        a1 = [2*i for i in range(1,n+1)]
        a2 = [a1[i]-1 for i in range(len(a1))]
        a2[-1]+= n
        a = a1+a2
        print(*a)