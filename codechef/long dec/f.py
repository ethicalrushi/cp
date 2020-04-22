from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    dic = defaultdict(lambda : 0)
  
    for i in range(n):
        a,b = [int(i) for i in input().split()]
        dic[a]+=1
        dic[b+0.1]-=1



    vals = sorted(list(dic.keys()))
    ans = 10**10
    s=0
    ans_arr = [-1]
    for val in vals:      
        curr = dic[val]        
        s += curr
        ans_arr.append(s)
    ans_arr.append(-1)
    
    #finding valley
    for i in range(1,len(ans_arr)-1):
        if ans_arr[i-1] > ans_arr[i] and ans_arr[i+1] > ans_arr[i]:
            ans = min(ans, ans_arr[i]) 
        



    if ans >= n-1 or ans == 10**9 :
        print(-1)
    else:
        print(ans)