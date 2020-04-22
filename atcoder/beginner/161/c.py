def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

n, k = [int(x) for x in input().strip().split()]

if n==0:
    res = 0
elif k==0:
    res=n
else:
    res = gcd(n,k)

if n>=k:
    if res==k:
        res=0

print(res)
