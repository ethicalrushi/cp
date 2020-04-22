n, m = [int(x) for x in input().strip().split()]
graph = {}
for i in range(m):
    u, v = [int(x) for x in input().strip().split()]
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

def dfs(n):
    visited[n] = 1
    if n in graph:
        for node in graph[n]:
            if node not in visited:
                dfs(node)
            dp[n-1] = max(dp[n-1],dp[node-1]+1)


visited = {}
dp = [0 for i in range(n)]

for i in range(1,n+1):
    if i not in visited:
        dfs(i)

print(max(dp))
         