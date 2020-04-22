
import random


def gen_arr(n):
    k = random.randint(1,n)
    a = []
    b = []
    for j in range(n-k):
        b.append(random.randint(1,100000))

    start = random.randint(1,100000)
    for i in range(k):
        a.append(start+i)
        iter = random.randint(0,len(b))
        a+=b[:iter]
        b = b[iter:]

    return a


def solve(arr):
    mod = 10**9+7
    aset = set(arr)
    res =0
    res_count = 0
    for a in arr:
        if a-1 not in aset:
            s=0
            count=0
            while a in aset:
                s+=a
                a+=1
                count+=1
            res = max(res, s)
            res_count = max(res_count, count)
    return res%mod



    

t = int(input())
with open('input/input03.txt','w') as inp:
    inp.write(str(t)+'\n')
    for _ in range(t):
        n = random.randint(1,100000)
        arr = gen_arr(n)
        arr_str = " ".join(str(a) for a in arr)
        inp.write(str(len(arr))+'\n')
        inp.write(arr_str+'\n')

        res = solve(arr)
        op = open('output/output03.txt','a')
        op.write(str(res)+'\n')
        op.close()






# Multiple stacks are possible for this collection of cards.<br>
# Let's consider 2 stacks as follows-<br>
# First- 1,5,3,2,4 since (1,2,3,4,5 are consecutive). Bid=15 <br>
# Second- 9,7,8 since(7,8,9 are consecutive). Bid=24<br>
# Since no stack would form bid higher than 24 in this case, 24 is the answer.<br>

# Note that the order of cards in given array doesn't matter as long as they form a consecutive stack.<br>
# Trivial Note: 1 and 1 are not consecutive.