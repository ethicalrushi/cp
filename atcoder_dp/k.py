n, k = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
a.sort()
dp = {} #determines whether dp[k] is a winning position or not
for i in range(k+1):
    dp[i] = False

for e in a:
    dp[e] = True

for i in range(a[0],k+1):
    for j in a:
        if i-j in dp:
            dp[i] = dp[i] or not(dp[i-j]) #if previous is true this is false
                                          #taken or to get best case of all optimality

if dp[k] is False:
    print('Second')
else:
    print('First')
