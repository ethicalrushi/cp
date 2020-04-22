def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        if (prime[p] == True): 
            
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    res = []
    for p in range(2, n): 
        if prime[p]: 
            res.append(p)

    return res

primes = SieveOfEratosthenes(340)
print(primes[:12])
print(len(primes))

t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    arr = list(set(a))

    dic = {}
    flag = [None for i in range(1010)]
    i = 0
    for e in arr:
        for prime in primes:
            if e%prime==0:
                if flag[e] is None:
                    flag[e] = True

                if flag[e] is True:
                    flag[e] = False

                if prime not in dic:
                    dic[prime] = [[],0]
                dic[prime][0].append(e)
                dic[prime][1]+=1

        i+=1

    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1][1], reverse=True)}
    print(dic)
    col = {}
    ck= 1
    for d in dic:
        if len(dic[d][0])==1:
            if flag[dic[d][0][0]] is True:
                col[dic[d][0][0]] = ck
        




    

    
    

                

    

