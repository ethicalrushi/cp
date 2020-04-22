from math import log2, floor

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    res = []
    for p in range(n + 1):  
        if prime[p]: 
            res.append(p)
    return res

prime = SieveOfEratosthenes(10**3+5)
pow2 = [pow(2,i) for i in range(21)]

#function to calculate power of primes for a number
def assign_factors(n): 
    res = {}
    for i in range(len(prime)):
        count=0
        while n%prime[i]==0:
            n=n//prime[i]
            count+=1
        res[prime[i]]=count
    
    if n>1:
        res[n]=1
    
    return res

def preprocess(arr): #O(nlogn)
    n = len(arr)
    l = floor(log2(n))+1

    sparse_table = [[None for j in range(l)] for i in range(n)] #store both minimum and it's index
    for i in range(n):
        sparse_table[i][0] = (arr[i], i)

    j=1
    while pow2[j]<=n:
        for i in range(n):
            nx_idx = i+pow2[j-1]
            if i+pow2[j]<=n:
                if sparse_table[i][j-1][0]<sparse_table[nx_idx][j-1][0]:
                    sparse_table[i][j] = sparse_table[i][j-1]
                else:
                    sparse_table[i][j] = sparse_table[nx_idx][j-1]

        j+=1

    return sparse_table


def minimum_query(s,e, sparse_table): #O(1)
    l = e-s+1
    k = floor(log2(l))
    if sparse_table[s][k][0]<sparse_table[e-pow2[k]+1][k][0]:
        return sparse_table[s][k][1]
    return sparse_table[e-pow2[k]+1][k][1]



mod = 10**9+7
t = int(input())
for _ in range(t):
    n = int(input())

    if n==1:
        a =  [int(x) for x in input().strip().split()]
        dicres = assign_factors(a[0])
        res=1

        for d in dicres:
            res = ((res%mod)*(dicres[d]+1)%mod)%mod
        

        q = int(input())
        for p in range(q):
            u, v = [int(x) for x in input().strip().split()]
            print(res)

    else:

        tree = [[] for i in range(n+1)]
        for i in range(n-1):
            u, v= [int(x) for x in input().strip().split()]
            tree[u].append(v)
            tree[v].append(u)

        a = [int(x) for x in input().strip().split()]
        
        factors = [0,] #1 indexed

        for e in a: #precomputing factors for all costs
            factors.append(assign_factors(e))    

        #Maintain product along the path in this from root to node in factors
        cost = [None for i in range(n+1)]

        def dicmerge(dic1, dic2): #helper function
            dic = {}
            for d in dic1:
                if d in dic2:
                    dic[d] = dic1[d]+dic2[d]
                else:
                    dic[d] = dic1[d]
            
            for d in dic2:
                if d not in dic:
                    dic[d] = dic2[d]
            return dic

        def compute_cost(curr, prev, prevfactor): #normal dfs
            
            stack = [(curr, prev, prevfactor)]
            while len(stack)>0:
                curr, prev, prevfactor = stack[-1]
                dic = dicmerge(prevfactor, factors[curr])
                cost[curr] = dic
                stack.pop()
                for i in range(len(tree[curr])):
                    if tree[curr][i]!=prev:
                        stack.append((tree[curr][i], curr, cost[curr]))

        depth = []
        euler_tour = []
        ind = {}

        def dfs(curr, curr_depth):  #implementation using stack
            stack = [(curr,curr_depth)]
            ptr = [0 for i in range(n+1)]
            parent = [None for i in range(n+1)]

            while len(stack)>0:
                curr, curr_depth = stack[-1]
                depth.append(curr_depth)
                euler_tour.append(curr)

                stack.pop() #remove current node

                k = len(tree[curr])
                while ptr[curr]<k and tree[curr][ptr[curr]]==parent[curr]:
                    ptr[curr]+=1

                if ptr[curr]==k: #go up
                    if parent[curr] is not None: #to avoid root error
                        stack.append((parent[curr],curr_depth-1))
                    else:
                        return #completed
                else: #go down
                    node = tree[curr][ptr[curr]]
                    stack.append((node, curr_depth+1))
                    ptr[curr]+=1
                    parent[node] = curr
        

        initfactor = {}
        compute_cost(1,0, initfactor)  #precalculating cost for each node

        dfs(1,0) #create euler tour and depth array

        l = len(euler_tour)
        for i in range(l): #caching indices for O(1) query 
            if euler_tour[i] not in ind:
                ind[euler_tour[i]] = i

        sparse_table = preprocess(depth)

        def lca(u, v):
            i = ind[u]
            j = ind[v]

            if i>j:
                i,j = j,i
            
            k = minimum_query(i,j,sparse_table)

            return euler_tour[k]

        q = int(input())

        for i in range(q):
            u, v = [int(x) for x in input().strip().split()]
            pivot = lca(u,v)

            dicv = cost[v]
            dicu = cost[u]
            dicpiv = cost[pivot]
            dicfac = factors[pivot]


            dic1 = {}
            for d in dicv:
                if d in dicpiv:
                    dic1[d] = dicv[d]-dicpiv[d]
                else:
                    dic1[d] = dicv[d]
            
            dic2 = {}

            for d in dicu:
                if d in dicpiv:
                    dic2[d] = dicu[d]-dicpiv[d]
                else:
                    dic2[d] = dicu[d]

            
            dicf = dicmerge(dic1, dic2)
            dicres = dicmerge(dicf, dicfac)

            res=1

            for d in dicres:
                res = ((res%mod)*(dicres[d]+1)%mod)%mod
            
            print(res%mod)
