import bisect

n = int(input())
s = input()

dic = {}
dic['R'] = []
dic['G'] = []
dic['B'] = []

for i in range(n):
    dic[s[i]].append(i)

rem = {}

rem['G'] = ['R', 'B']
rem['B'] = ['R','G']
rem['R'] = ['B', 'G']

res=0

for i in range(n):
    neigh1 = rem[s[i]][0]
    neigh2 = rem[s[i]][1]
    ind = bisect.bisect_right(dic[neigh1],i)
    for j in range(ind, len(dic[neigh1])):
        node = dic[neigh1][j]
        nind = bisect.bisect_right(dic[neigh2],node)

        l = max(0,len(dic[neigh2])-nind)

        diff = node-i
        if node+diff>=nind and node+diff<n and s[node+diff]==neigh2:
            l-=1

        res+=l

    ind = bisect.bisect_right(dic[neigh2],i)
    for j in range(ind, len(dic[neigh2])):
        node = dic[neigh2][j]
        nind = bisect.bisect_right(dic[neigh1],node)

        l = max(0,len(dic[neigh1])-nind)

        diff = node-i
        if node+diff>=nind and node+diff<n and s[node+diff]==neigh1:
            l-=1

        res+=l

print(res)

    
        



