import bisect
t = int(input())

def node_order_bfs(i,tree,node,arr):
    t=0
    queue = []
    queue.append(i)
    visited = {} 
    visited[i]=True
    while len(queue)!=0:
        curr = queue.pop(0)
        node[curr] = arr[t]
        t+=1
        for child in tree[curr]:
            if child not in visited:
                queue.append(child)
                visited[child]=True


# def node_order_dfs(i,tree,parent,node,arr):
#     global col
#     print(col,i)
#     node[i] = arr[col]
#     col+=1
#     for child in tree[i]:
#         if child!=parent and child not in node:
#             node_order_dfs(child,tree,i,node,arr)

def count_edges(edges,mn, dic):
    res =0
    ind = bisect.bisect_right(edges,mn)
    # print(u,v,mn,ind)
    if ind>0:
        while ind-1>=0 and ind-1 in dic:
            ind-=1
        if ind-1>=0:
            dic[ind-1]=1
        else:
            res+=1
    else:
        res+=1
    return res

def solve(i, edges, node, tree):
    t=0
    queue = []
    queue.append(i)
    visited = {} 
    visited[i]=True
    ans = 0
    dic = {}
    while len(queue)!=0:
        curr = queue.pop(0)
        mx = node[curr]
        for child in tree[curr]:
            if child not in visited:
                queue.append(child)
                visited[child]=True
                mn = node[child]
                temp=count_edges(edges,mn,dic)
                if temp==1:
                    temp+=count_edges(edges,mx,dic)
                # print(mn,mx,temp,dic)
                ans+=temp

    return ans


        
for _ in range(t):
    n = int(input())
    tree = {}
    edges = []
    node = {}
    edge_list = []
    #constructing tree and edges list
    for i in range(n-1):
        u,v,e = [int(x) for x in input().strip().split()]
        edge_list.append((u,v))
        edges.append(e)
        if u not in tree:
            tree[u] =[]
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)
    
    arr = [int(x) for x in input().strip().split()]
    arr.sort(reverse=True)
    col = 0

    #maximum degree node
    deg = 0
    for t in tree:
        if len(tree[t])>deg:
            mdegnode = t
            deg = len(tree[t])

    node_order_bfs(mdegnode,tree,node,arr)
    edges.sort()
    res = solve(mdegnode,edges,node,tree)
    print(res)
    # print(node)
    # print(edges)
