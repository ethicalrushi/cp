t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    dic = {}
    for i in range(n):
        a = [int(x) for x in input().strip().split()]
        arr.append(a[1:])

    coupled = set([])
    rem = []
    for i in range(n):
        for j in range(len(arr[i])):
            if arr[i][j] not in coupled:
                dic[i+1] = arr[i][j]
                coupled.add(arr[i][j])
                break
        if i+1 not in dic:
            rem.append(i+1) #girl
    
    if len(rem)==0:
        print("OPTIMAL")
    else:
        g1 = rem[0]
        for boy in range(1,n+1):
            if boy not in coupled:
                b1 = boy
                break
        
        print("IMPROVE")
        print(g1,b1)



        
    
