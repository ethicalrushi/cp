
def search(nums: list, target: int) -> int:
    n = len(nums)

    l, r = 0, n - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    # gets the index of minimum element
    temp = l 

    # assigning new left or right index
    l, r = 0, n - 1
    if temp != 0:
        if target > nums[temp] and target >= nums[l]:
            r = temp - 1
        else:
            l = temp
    else:
        # temp = 0 indicates that the array is already sorted 
        # hence left and right are at extreme ends
        l, r = 0, n - 1

    # Normal binary search in that slice of array
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    q = int(input())
    for i in range(q):
        tar = int(input())
        print(search(arr,tar))