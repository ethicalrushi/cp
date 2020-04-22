tree = {}
n = int(input())
for i in range(1,n+1):
    tree[i] = []

for i in range(n-1):
    u, v= [int(x) for x in input().strip().split()]
    tree[u].append(v)
    tree[v].append(u)


depth = [None for i in range(n+1)]
def dfs(i):
    stack = [(i,1, -1)]
    while len(stack)>0:
        curr, curr_depth, prev = stack[-1]
        stack.pop()
        depth[curr] = curr_depth
        for node in tree[curr]:
            if node!=prev:
                stack.append((node, curr_depth+1, curr))

for i in range(1,n+1):
    if len(tree[i])==1:
        root = i
        break

dfs(root)
mn = 1
for i in range(1,n+1):
    if len(tree[i])==1 and i!=root:
        if depth[i]%2==0:
            mn=3

mx = n-1
for i in range(1,n+1):
    ct=0
    for node in tree[i]:
        if len(tree[node])==1:
            ct+=1

    if ct>=2:
        mx-=(ct-1)

print(mn, mx)
    

    
