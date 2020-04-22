t = int(input())
for _ in range(t):
    n = int(input())
    a = [str(x) for x in input().strip().split()]
    dic = {}
    i = 0
    flag=False
    for e in a:
        if e not in dic:
            dic[e] = []
        else:
            top = dic[e][-1]
            if i-top>1:
                flag=True
                break
        dic[e].append(i)
        i+=1

    

    if flag:
        print("YES")
    else:
        print("NO")