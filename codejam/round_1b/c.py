t = int(input())
for _ in range(t):
    x, y = [int(x) for x in input().strip().split()]
    dp = [[[None for k in range(16)] for j in range(210)] for i in range(210)]
    def solve(i, j, k, res):
        # print(i,j,k,res)
        if i==x and j==y:
            return True, res, k

        # if (i-(2**k-1)>x) or (j-(2**k-1)>y):
        #     return False, res, k

        if k>=16:
            return False, res, k

        if dp[i][j][k]:
            return dp[i][j][k]

        if i==x:
            f1 = solve(i, j+2**(k-1), k+1, res+'N')
            f2 = solve(i, j-2**(k-1), k+1, res+'S')
            if f1[0] and f2[0]:
                if f1[2]<f2[2]:
                    dp[i][j][k]= f1
                else:
                    dp[i][j][k]= f2
            elif f1[0]:
                dp[i][j][k]= f1
            elif f2[0]:
                dp[i][j][k]= f2
            else:
                dp[i][j][k]= [False, res, k]

        elif j==y:
            f1 = solve(i+2**(k-1), j, k+1, res+'E')
            f2 = solve(i-2**(k-1), j, k+1, res+'W')
            if f1[0] and f2[0]:
                if f1[2]<f2[2]:
                    dp[i][j][k]= f1
                else:
                    dp[i][j][k]= f2
            elif f1[0]:
                dp[i][j][k]= f1
            elif f2[0]:
                dp[i][j][k]= f2
            else:
                dp[i][j][k]= [False, res, k]

        else:
            f1 = solve(i+2**(k-1), j, k+1, res+'E')
            f2 = solve(i-2**(k-1), j, k+1, res+'W')
            f3 = solve(i, j+2**(k-1), k+1, res+'N')
            f4 = solve(i, j-2**(k-1), k+1, res+'S')

            arr = [f1,f2,f3,f4]
            mn = 10**10
            id = -1
            for i in range(4):
                if arr[i][0]:
                    if arr[i][-1]<mn:
                        mn = arr[i][-1]
                        id = i
            if id>=0:
                dp[i][j][k]= arr[id]
            else:
                dp[i][j][k]= [False, res, k]

        return  dp[i][j][k]

    print(dp[-1][-2][2])
    if x==0 and y==0:
        res_string=""
    else:
        ans = solve(0,0,1, "")
        if ans[0]:
            res_string = ans[1]
        else:
            res_string = "IMPOSSIBLE"

    res = "Case #{}: {}".format(_+1, res_string)
    print(res)

