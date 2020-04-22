"""
nlogn complexity 
solution ises segment tree to do max range queries

We sort array by width
for each rectangle find rightmost rectangle having height greater than it in logn using seg tree
"""



from math import ceil, log2

n = int(input())
a=[]
for i in range(n):
    temp = [int(X) for X in input().strip().split()]
    a.append(temp)

a.sort()
for i in range(n):
    a[i] = [a[i], i]

dic = {}

heights = [a[i][0][1] for i in range(n)]
heights = list(set(heights))
heights.sort()

for i in range(n):
    h = a[i][0][1]
    if h not in dic:
        dic[h] = [i,0]
    dic[h][0] = max(dic[h][0],i)

b = []
ind=0

for e in heights:
    dic[e][1] = ind
    b.append(dic[e][0])
    ind+=1

m = len(b)
x = (int)(ceil(log2(m)));  
max_size = 2 * (int)(2**x) - 1
tree = [0 for i in range(max_size)]

def construct_segtree(s,e,b,i):
    if s==e:
        tree[i] = b[s]
        return b[s]
    
    mid = (s+e)//2
    tree[i] = max(construct_segtree(s,mid,b,2*i+1), construct_segtree(mid+1,e,b,2*i+2))
    return tree[i]

def query(s,e,i,qs,qe):
    if qe<s or qs>e:
        return 0 #min
    
    if qs<=s and qe>=e:
        return tree[i]

    mid = (s+e)//2
    return max(query(s,mid,2*i+1,qs,qe), query(mid+1, e, 2*i+2, qs, qe))

construct_segtree(0,m-1,b,0)

res=0
for i in range(n):
    w, h = a[i][0]
    ind = dic[h][1]
    if ind==n-1:
        res+=1
    else:
        mxidx = query(0,m-1,0,ind+1,m-1)
        w1 = a[mxidx][0][0]
        if w1<=w:
            res+=1

print(res)