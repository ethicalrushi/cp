n = int(input())
a = [int(x) for x in input().strip().split()]

def divide(a):
    l = len(a)
    la = a[:l//2]
    lb = a[l//2:]
    return la, lb

def merge(a, b, count):
    i = 0
    j= 0
    l1 = len(a)
    l2 = len(b)
    # print(a,b)
    while i<l1 and j<l2:
        if a[i]<b[j]:
            i+=1
        else:
            # print('me')
            
            count+=1*(l1-i)
            # print(j,i,l1, count)
            j+=1
            i+=1
            if i>=l1-1:
                i-=1
    return count

def solve(a, count):
    l = len(a)
    if l==1:
        return count
    else:
        la, lb = divide(a)
        c1 = solve(la, count)
        c2 = solve(lb, count)
        count+=merge(la,lb,count)+c1+c2
    return count

print(solve(a,0))