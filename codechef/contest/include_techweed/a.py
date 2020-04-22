t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().strip().split()]
    s = input()
    dic = {}

    for e in s:
        if e not in dic:
            dic[e] = 0
        dic[e]+=1
    
    flag = True

    # print(dic)
    for e in dic:
        if dic[e]%2!=0:
            flag=False
        
        elif dic[e]//2>k:
            flag=False

        else:
            pass

    if flag:
        print("YES")
    else:
        print("NO")