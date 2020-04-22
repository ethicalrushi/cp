from math import ceil, log2
arr= [int(x) for x in input().strip().split()]
n = len(arr)
seg_size = 2*n-1
MIN = -10**10
seg = [MIN for i in range(seg_size)]

def create_tree(arr,seg,low,high, pos):
    if low==high:
        seg[pos] = arr[low]
        return seg[pos]
    
    mid = (low+high)//2
    seg[pos] = max(create_tree(arr,seg,low,mid,2*pos+1),create_tree(arr,seg,mid+1,high,2*pos+2))
    return seg[pos]

def query(seg,qs,qe,low,high,pos):
    if qs<=low and qe>=high: #total overlap
        return seg[pos]
    
    if qs>high or qe<low: #no overlap
        return MIN

    mid = (low+high)//2
    return max(query(seg,qs,qe,low,mid,2*pos+1),query(seg,qs,qe,mid+1,high,2*pos+2))

create_tree(arr,seg,0,n-1,0)

t = int(input())
for _ in range(t):
    u,v = [int(x) for x in input().strip().split()]
    print(query(seg,u,v,0,n-1,0))


