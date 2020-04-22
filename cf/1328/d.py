t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]

    res = [0 for i in range(n)]
    count = 1
    cc=1
    res[0] = 1
    flag=False
    for i in range(1,n):
        prev = a[i-1]
        curr = a[i]

        if curr==prev:
            # print('i')
            flag=True
            ind = i
            res[i]=res[i-1]
        else:
            # print('j')
            if count==1:
                count+=1
            if cc==1:
                res[i] = 2
                cc = 2
            else:
                res[i]=1
                cc=1
 
    if res[0]!=res[-1] or a[0]==a[-1]:
        # print('u')
        print(count)
        print(*res)

    else:
        if flag:
            for i in range(ind, n):
                if res[i]==1:
                    res[i]=2
                else:
                    res[i]=1
            print(count)
            print(*res)
        else:
            print(3)
            res[-1]=3
            print(*res)


