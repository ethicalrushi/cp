from math import log2, floor

depth = []
euler_tour = []
ind = {}

def preprocess(arr): #O(nlogn)
    n = len(arr)
    l = floor(log2(n))+1

    sparse_table = [[None for j in range(l)] for i in range(n)] #store both minimum and it's index
    for i in range(n):
        sparse_table[i][0] = (arr[i], i)

    j=1
    while 2**j<=n:
        for i in range(n):
            nx_idx = i+2**(j-1)
            if i+2**j<=n:
                if sparse_table[i][j-1][0]<sparse_table[nx_idx][j-1][0]:
                    sparse_table[i][j] = sparse_table[i][j-1]
                else:
                    sparse_table[i][j] = sparse_table[nx_idx][j-1]

        j+=1

    return sparse_table


def minimum_query(s,e, sparse_table): #O(1)
    l = e-s+1
    k = floor(log2(l))
    if sparse_table[s][k][0]<sparse_table[e-2**k+1][k][0]:
        return sparse_table[s][k][1]
    return sparse_table[e-2**k+1][k][1]


n = int(input()) #no of nodes
tree = {}
for i in range(n-1):  #building the tree
    u, v = [int(x) for x in input().strip().split()] #edges
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    
    tree[u].append(v)
    tree[v].append(u)

# vis = set([])
# def dfs(curr, prev, prev_depth):    #recursive implementation
#     curr_depth = prev_depth+1
#     depth.append(curr_depth)
#     euler_tour.append(curr)
#     vis.add(curr)
#     for node in tree[curr]:
#         if node not in vis:
#             dfs(node,curr,curr_depth)
#             depth.append(curr_depth)
#             euler_tour.append(curr)

"""
tree linearization - cinverting to euler walk and corresponding depth array using stack
"""
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


dfs(1,0) 
print(euler_tour)
print(depth)

l = len(euler_tour)
print(l)
for i in range(l):
    if euler_tour[i] not in ind:
        ind[euler_tour[i]] = i

sparse_table = preprocess(depth)

def lca(u, v):
    i = ind[u]
    j = ind[v]

    if i>j:
        i,j = j,i
    
    k = minimum_query(i,j,sparse_table) #return index of least depth node from all nodes in path between u and v

    return euler_tour[k] #return the node

while True:
    u, v = [int(x) for x in input().strip().split()]
    print(lca(u,v))