t = int(input())
for _ in range(t):
    n,m,k = [int(x) for x in input().strip().split()]
    answers = []
    for i in range(n):
        temp = [int(x) for x in input().strip().split()]
        dic = {}
        mx=0
        ans=temp[0]
        for t in temp:
            if t not in dic:
                dic[t]=0
            dic[t]+=1
            if dic[t]>mx:
                mx=dic[t]
                ans=t
        answers.append(ans)
    
    print(*answers)

