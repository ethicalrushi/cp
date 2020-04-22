n, k= [int(x) for x in input().strip().split()]
tree = {}
for i in range(1,n+1):
    tree[i] = []

for i in range(n-1):
    u, v= [int(x) for x in input().strip().split()]
    tree[u].append(v)
    tree[v].append(u)

dp = [None for  i in range(n+1)]
depth = [None for  i in range(n+1)]

def subtree(node, par):
    dp[node] = 1
    for child in tree[node]:
        if child!=par:
            dp[node]+=subtree(child, node)

    return dp[node]

def dfs(node, d, par):
    depth[node] = d
    for child in tree[node]:
        if child!=par:
            dfs(child, d+1, node)

subtree(1,-1)
dfs(1,0,-1)

arr = [depth[i]-(dp[i]-1) for i in range(1,n+1)]
arr.sort(reverse=True)
res = sum(arr[:k])
print(res)