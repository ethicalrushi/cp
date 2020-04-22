from math import log2, floor

def preprocess(arr): #O(nlogn)
    n = len(arr)
    l = floor(log2(n))+1

    sparse_table = [[None for j in range(l)] for i in range(n)] #store both minimum and it's index
    for i in range(n):
        sparse_table[i][0] = (arr[i], i)

    j=1
    while 2**j<=n:
        for i in range(n):
            nx_idx = i+2**(j-1)
            if i+2**j<=n:
                if sparse_table[i][j-1][0]<sparse_table[nx_idx][j-1][0]:
                    sparse_table[i][j] = sparse_table[i][j-1]
                else:
                    sparse_table[i][j] = sparse_table[nx_idx][j-1]

        j+=1

    return sparse_table


def minimum_query(s,e, sparse_table): #O(1)
    l = e-s+1
    k = floor(log2(l))
    return min(sparse_table[s][k][0], sparse_table[e-2**k+1][k][0]) #first 2**k elements of range and last k elements, they possibly overlap



a = [int(x) for x in input().strip().split()]
table = preprocess(a)

for t in table:
    print(t)

while True:
    u, v = [int(x) for x in input().strip().split()]
    print(minimum_query(u,v, table))

