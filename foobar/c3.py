n = int(input())
map = []
for _ in range(n):
    temp = [int(x) for x in raw_input().strip().split()]
    map.append(temp)

h = len(map)
w = len(map[0])

dp = [[[None, None]for i in range(w)] for j in range(h)]

inf = 10**10

def solve(i, j, flag):
    if dp[i][j][flag] is not None:
        return dp[i][j][flag]

    if i==0 and j==0:  #base condition
        return 1

    l = (max(0,i-1), j)
    r = (min(h-1, i+1), j)
    u = (i, max(0, j-1))
    d = (i, min(w-1, j+1))

    neighbours = [l,r,u,d]

    dp[i][j][flag] = inf

    for node in neighbours:
        if node[0]!=i or node[1]!=j: #new node
            if map[node[0]][node[1]]==0: #no need to change flag
                dp[i][j][flag] = min(dp[i][j][flag], 1+solve(node[0], node[1], flag))
            elif map[node[0]][node[1]]==1 and flag==0: #we already removed one obstacle so return inf
                dp[i][j][flag] = min(dp[i][j][flag], inf)
            else: #flag=1 we remove the obstacle and urn flag 0
                dp[i][j][flag] = min(dp[i][j][flag], 1+solve(node[0], node[1], 0))
    
    return dp[i][j][flag]

res = solve(h-1, w-1, 1) #we don't remove the obstacle here
print(res)

