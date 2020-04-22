import bisect
t = int(input())
for _ in range(t):
    s = input()
    x = input()

    dic = {}

    i=0
    for e in s:
        if e not in dic:
            dic[e] = [[],0]
        dic[e][0].append(i)
        i+=1

    # print(dic)


    res = 1
    gi = 0
    for char in x:
        # print(char, gi, dic[char][1])
        if char not in dic:
            res = -1
            break
        
        ind = dic[char][1]
        li = bisect.bisect_left(dic[char][0],gi)
        if(li<len(dic[char][0])):
            dic[char][1] = li+1
            gi = dic[char][0][li]+1
        else:
           
            dic[char][1] = 1
            gi = dic[char][0][0]+1
            res+=1

        # print(char, gi, li, dic[char][1])
    
    print(res)

        
    
