t = int(input())
for _ in range(t):
    n = int(input())
    res = n//2
    arr = []
    if n==1:
        res=1
        arr.append([1,1])
    elif n==2:
        res=1
        arr.append([1,2])
    else:
        arr.append([3,1,2,3])
        mx=0
        for i in range(4,n,2):
            temp = [2,i,i+1]
            mx=i+1
            arr.append(temp)

        if mx!=n:
            arr.append([1,n])
        res=len(arr)
    print(res)
    for i in range(res):
        print(*arr[i])
    