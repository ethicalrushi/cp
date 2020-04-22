from collections import deque
t = int(input())



for _ in range(t):
    n,m,a,b,c = [int(x) for x in input().strip().split()]
    graph = {}

    p = [int(x) for x in input().strip().split()]

    for i in range(m):
        u, v = [int(x) for x in input().strip().split()]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        
        graph[u].append(v)
        graph[v].append(u)


    def min_bfs(src, des):
        vis = set([])
        q = deque()
        q.append((src,[]))
        while len(q)!=0:
            curr, temp = q.popleft()
            vis.add(curr)
            if curr==des:
                return temp
            for node in graph[curr]:
                if node not in vis:
                    q.append((node,temp+[curr]))

    def bfs(src, des):
        vis = set([])
        q = deque()
        q.append((src,[]))
        res = []
        while len(q)!=0:
            curr, temp = q.popleft()
            vis.add(curr)
            if curr==des:
                res.append(temp)
            else:
                for node in graph[curr]:
                    if node not in vis:
                        q.append((node,temp+[curr]))

        return res

    resab = min_bfs(a,b)
    resbc = bfs(b,c)
    print(resab)
    print(resbc)

    
