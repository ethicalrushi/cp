t = int(input())
for _ in range(t):
    x, y = [int(x) for x in input().strip().split()]

    def solve(i, j, k, res):
        if i==x and j==y:
            return True, res, k

        if k>=9:
            return False, res, k

        if i==x:
            f1 = solve(i, j+2**(k-1), k+1, res+'N')
            f2 = solve(i, j-2**(k-1), k+1, res+'S')
            if f1[0] and f2[0]:
                if f1[2]<f2[2]:
                    return f1
                else:
                    return f2
            elif f1[0]:
                return f1
            elif f2[0]:
                return f2
            else:
                return [False, res, k]

        elif j==y:
            f1 = solve(i+2**(k-1), j, k+1, res+'E')
            f2 = solve(i-2**(k-1), j, k+1, res+'W')
            if f1[0] and f2[0]:
                if f1[2]<f2[2]:
                    return f1
                else:
                    return f2
            elif f1[0]:
                return f1
            elif f2[0]:
                return f2
            else:
                return [False, res, k]

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
                return arr[id]
            else:
                return [False, res, k]



    ans = solve(0,0,1, "")
    if ans[0]:
        res_string = ans[1]
    else:
        res_string = "IMPOSSIBLE"

    res = "Case #{}: {}".format(_+1, res_string)
    print(res)

