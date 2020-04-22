from collections import deque

n = int(input())

tree = {}
node = {}

for i in range(1,n+1):
    tree[i] = []
    node[i] = -1


for i in range(n-1):
    u, v = [int(x) for x in input().strip().split()]
    tree[u].append(v)
    tree[v].append(u)

node[1] = 0
stack = deque([1,])
while len(stack)!=0:
    root = stack.popleft()
    val = node[root]
    

    for child in tree[root]:
        if node[child]==-1:
            node[child] = val+1
            stack.append(child)

# print(node)
q = int(input())
for _ in range(q):
    flag = False
    x, y, a, b, k = [int(x) for x in input().strip().split()]
    d1 = abs(node[a]-node[b])
    d2 = abs(node[a]-node[x])+1+abs(node[b]-node[y])
    d3 = abs(node[a]-node[y])+1+abs(node[b]-node[x])

    if d1<=k:
        r = k-d1
        if r%2==0:
            flag=True
    
    if d2<=k:
        r = k-d2
        if r%2==0:
            flag = True
    
    if d3<=k:
        r = k-d3
        if r%2==0:
            flag = True

    if flag:
        print("YES")
    else:
        print("NO")







