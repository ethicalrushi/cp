def solve():
    N, M, A, B = map(int, input().split())
    roads = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    A -= 1
    B -= 1
    
    adj = [[] for _ in range(N)]
    for a, b in roads:
        adj[a].append(b)
        adj[b].append(a)
    
    def dfs(start, invalid):
        Q = [start]
        visited = set()
        while Q:
            q = Q.pop()
            for next in adj[q]:
                if next == invalid or next in visited:
                    continue
                else:
                    visited.add(next)
                    Q.append(next)
        return visited-{start}
    
    set_A = dfs(A, B)
    set_B = dfs(B, A)
    print(len(set_A-set_B)*len(set_B-set_A))
    
    
T = int(input())
for _ in range(T):
    solve()