t = int(input())

for _ in range(t):
    arr = [0 for i in range(11)]
    n = int(input())
    for i in range(n):
        p,s = [int(x) for x in input().strip().split()]
        arr[p-1] = max(arr[p-1],s)

    res = sum(arr)-arr[8]-arr[9]-arr[10]
    print(res)
        
        