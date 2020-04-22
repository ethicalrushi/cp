n = int(input())

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    res = []
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            res.append(p)

    return res


primes = SieveOfEratosthenes(1000)
pset = set(primes)

# k = int(input())
# while(True):
#     print(primes[k-1])
#     k = int(input())


m1 = None
m2 = None
for p in primes:
    if n%p==0:
        e = n//p
        if e in pset:
            m1, m2 = p,e
            break

res = ''
if m1 is not None and m2 is not None:
    if m1>m2:
        m1, m2 = m2,m1
    
    res+=str(m1)+str(m2)

print(res)



