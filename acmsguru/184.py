import sys
arr = []
for line in sys.stdin:
    arr += [int(x) for x in line.strip().split()]
print(arr)
# p,m,c,k,r,v = [ int(x) for x in input().strip().split()]
