

h, w = [int(x) for x in input().strip().split()]
map = []
for _ in range(h):
    temp = [int(x) for x in input().strip().split()]
    map.append(temp)
    
dp = [[[None, None] for i in range(w)] for j in range(h)]

inf = 10**10

def solve(i, j, flag):
    if dp[i][j][flag] is not None:
        return dp[i][j][flag]

    if i==h-1 and j==w-1:  #base condition
        if map[i][j]=='.' and flag==0:
            return 0
        if map[i][j]=='#' and flag==1:
            return 0
        return 1

    r = (min(h-1, i+1), j)
    d = (i, min(w-1, j+1))

    neighbours = [r,d]
    dp[i][j][flag] = inf #initialization

    for node in neighbours:
        if node[0]!=i or node[1]!=j: #new node
            if map[node[0]][node[1]]=='.' and flag==0: #no need to change 
                dp[i][j][flag] = min(dp[i][j], solve(node[0], node[1]))
            elif map[node[0]][node[1]]=='#' and flag==1:
                dp[i][j][flag] = min(dp[i][j], solve(node[0], node[1]))
            else:
                i1 = node[0]
                j1 = node[1]
                if flag==0:
                    f1 = 1
                else:
                    f1 = 0
                dp[i][j][flag] = min(dp[i][j], 1+solve(i1, j1, f1))

                

    
    return dp[i][j][flag]

if map[0][0]=='.':
    res = solve(0,0,0) #no need to reverse
else:
    res = solve(0,0,1) #set flag to reverse

print(res)

