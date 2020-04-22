
n = int(input())
color = [None for i in range(n)]
tree = {}
res = 0
et = []
for i in range(n-1):
    u, v = [int(x) for x in input().strip().split()]
    et.append((u,v))
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[u].append(v)
    tree[v].append(u)
    res = max(res, len(tree[u]),len(tree[v]))

# for i in range(1,n+1):
#     if i not in tree:
#         tree[i] = []

edge = {}
color[0] = 0

for i in range(1,n+1):
    for v in tree[i]:
        if v>i:
            tc = color[i-1]+1
            if tc>res:
                tc = tc%res
            color[i-1] = tc
            color[v-1] = tc
            if i not in edge:
                edge[i] = {}
            if v not in edge[i]:
                edge[i][v] = {}
            edge[i][v] = tc

# res = max(edge)
print(res)
for e in et:
    print(edge[e[0]][e[1]])


