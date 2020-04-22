n = int(input())
a = [int(x) for x in input().strip().split()]

mat = []
ind = []
for i in range(n):
    temp = []
    for j in range(n):
        curr = abs(i-j)*a[i] #put i at j
        temp.append(curr)
    ntemp = [(temp[i], i) for i in range(n)]
    ntemp.sort(reverse=True)
    nind = [e for n,e in ntemp]
    mat.append(temp)
    ind.append(nind)

ans = [None for i in range(n)]
index = [set([]) for i in range(n)]
mx = 0

print(mat)

print(ind)

for j in range(n):
    ans[j] = mat[0][j]
    index[j].add(j)
    mx= max(mx, ans[j])

# sel_ind = [[None for i in range(n)] for j  in range(n)]
for i in range(1,n):
    temp = [None for i in range(n)]
    for j in range(n):
        temp[j]= ans[j]
        # mx_r_idx = -1
        for k in ind[i]:
            if k not in index[j]:
                mx_r_idx = k
                break
        # r1, r2 = ind[i][0], ind[i][1]

        # mx_r_idx = r1
        # if r1 in index[j]:
        #     mx_r_idx = r2

        temp[j]+=mat[i][mx_r_idx]
        index[j].add(mx_r_idx)
        mx = max(mx, temp[j])
    ans = temp

print(mx)


