n, k = [int(x) for x in input().strip().split()]
arr = []
for i in range(k):
    arr.append(input().strip())

ind = n%k
if ind==0:
    print(arr[-1])
else:
    print(arr[ind-1])