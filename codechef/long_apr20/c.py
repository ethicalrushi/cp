def count_factors(x):
    count=0

    while x%2==0:
        x=x//2
        count+=1
        
    i=3
    while i*i<=x:
        while x%i==0:
            x=x//i
            count+=1
        
        i+=2

    if x>2:
        count+=1

    return count

t = int(input())
for _ in range(t):
    x,k = [int(x) for x in input().strip().split()]
    count = count_factors(x)

    if count>=k:
        print(1)
    else:
        print(0)
