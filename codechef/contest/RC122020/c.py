t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    a = [(a[i],i) for i in range(n)]
    a.sort()
    res=1
    prev=0
    prev_ind = -1
  
    i=0
    while i<n:
        if a[i][1]>prev_ind:
            prev_ind = a[i][1]
            prev = a[i][0]
            while i<n and a[i][0]==prev:
                i+=1
        else:
            prev = a[i][0]
            flag = False
            mn=a[i][1]
            while i<n and a[i][0]==prev:
                if a[i][1]>prev_ind:
                    prev_ind=a[i][1]
                    flag = True
                    break
                i+=1
            if flag:
                while i<n and a[i][0]==prev:
                    i+=1
            else:
                res+=1
                prev_ind=mn
    print(res)

