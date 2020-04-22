n, m = [int(x) for x in input().strip().split()]
strings = []
for _ in range(n):
    s = input()
    strings.append(s)


s_p = []
n = len(strings)
for i in range(n):
    if strings[i] == strings[i][::-1]:
        s_p.append(i)


pair = []
for i in range(n-1):
    for j in range(i+1, n):
        if strings[i] == strings[j][::-1]:
            pair.append((i,j))

res = ""
for p in pair:
    res+=strings[p[0]]

res1 = res[::-1]

p_set = set([])
for p in pair:
    if p[0] not in p_set:
        p_set.add(p[0])
    if p[1] not in p_set:
        p_set.add(p[1])


mid = ""
for ind in s_p:
    if ind not in p_set:
        mid = strings[ind]

ans = res+mid+res1
print(len(ans))
print(ans)








