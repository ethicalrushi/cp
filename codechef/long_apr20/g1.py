from math import log2, floor, gcd
from collections import Counter

import os
import sys
from io import BytesIO, IOBase

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


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
    
    return Counter(res)

class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


class LCA:
    def __init__(self, root, graph):
        self.time = [-1] * len(graph)
        self.path = [-1] * len(graph)
        P = [-1] * len(graph)
        t = -1
        dfs = [root]
        while dfs:
            node = dfs.pop()
            self.path[t] = P[node]
            self.time[node] = t = t + 1
            for nei in graph[node]:
                if self.time[nei] == -1:
                    P[nei] = node
                    dfs.append(nei)
        self.rmq = RangeQuery(self.time[node] for node in self.path)

    def __call__(self, a, b):
        if a == b:
            return a
        a = self.time[a]
        b = self.time[b]
        if a > b:
            a, b = b, a
        return self.path[self.rmq.query(a, b)]


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

        def compute_cost(curr, prev, prevfactor): #normal dfs
            
            stack = [(curr, prev, prevfactor)]
            while len(stack)>0:
                curr, prev, prevfactor = stack[-1]
                cost[curr] = prevfactor + factors[curr]
                stack.pop()
                for i in range(len(tree[curr])):
                    if tree[curr][i]!=prev:
                        stack.append((tree[curr][i], curr, cost[curr]))

        initfactor = Counter()
        compute_cost(1,0, initfactor)  #precalculating cost for each node

        q = int(input())

        lca = LCA(1,tree)

        for i in range(q):
            u, v = [int(x) for x in input().strip().split()]
            pivot = lca(u,v)

            dicv = cost[v]
            dicu = cost[u]
            dicpiv = cost[pivot]
            dicfac = factors[pivot]

            dic1 = dicv-dicpiv
            dic2 = dicu-dicpiv
            dicf = dic1+dic2
            dicres = dicf+dicfac

            res=1

            for d in dicres:
                res = ((res%mod)*(dicres[d]+1)%mod)%mod
            
            print(res%mod)