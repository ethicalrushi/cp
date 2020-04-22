####Incorrect logically############

n = int(input())
mod = 10**9+7

graph = {}
for i in range(n-1):
    u, v = [int(x) for x in input().strip().split()]

    if u not in graph:
        graph[u] =[]
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

#0-black, 1-white
def solve(i,parent,c):
    res=0
    flag = False
    if c==0:
        for node in graph[i]:
            if node!=parent:
                flag = True
                res+=solve(node,i,1)%mod

    else:
        for node in graph[i]:
            if node!=parent:
                flag = True
                res+=(solve(node,i,0)%mod+solve(node,i,1)%mod)%mod

    if flag:
        return res
    else: #leaf node
        return 1

ans = (solve(1,0,0)%mod + solve(1,0,1)%mod)%mod
print(ans)