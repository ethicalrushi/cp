def solve(p, s):
    dp = {}
    symb = {'*'}
    # print("trying for", s, p, len(s), len(p))
    def check(i,j, res_string):
        # print(i, j, res_string)
        if (i,j) in dp:
            return dp[i,j]
        
        # print(i,j)
        if j==len(p):
            if i==len(s):
                return True, res_string

        if j>len(p):
            return False, res_string
        
        if i>len(s):
            return False, res_string
        
        if j<len(p) and p[j] not in symb:
            if i<len(s) and s[i]==p[j]:
                dp[i,j] = check(i+1,j+1, res_string+s[i])
            else:
                if i<len(s) and s[i]=="*":
                    if j<len(p) and check(i,j+1,res_string+p[j])[0]:
                        dp[i,j] = check(i,j+1,res_string+p[j])
                    elif check(i+1,j,res_string)[0]:
                        dp[i,j] = check(i+1,j,res_string)
                    else:
                        dp[i,j] = [False, ""]
                else:
                    dp[i,j] = [False, ""]
                            

        elif j<len(p) and i<len(s) and p[j]=="*" and s[i]=="*":
            # if check(i+1, j+1, res_string+'*')[0]:
            #         dp[i,j] = check(i+1, j+1, res_string+'*')
            if j<len(p) and check(i,j+1,res_string+p[j])[0]:
                dp[i,j] = check(i,j+1,res_string+p[j])
            elif i<len(s) and check(i+1,j,res_string+s[i])[0]:
                dp[i,j] = check(i+1,j,res_string+s[i])
            else:
                dp[i,j] = [False, ""]
            

        elif j<len(p) and p[j]=="*":
            if check(i,j+1,res_string)[0]:
                dp[i,j] = check(i,j+1,res_string)
            elif i<len(s) and check(i+1,j,res_string+s[i])[0]:
                dp[i,j] = check(i+1,j,res_string+s[i])
            else:
                dp[i,j] = [False, ""]
            # dp[i,j][0] = check(i,j+1,res_string)[0] or check(i+1,j,res_string+s[i])[0]
        else:
            dp[i, j] = [False, ""]
            
        return dp[i,j]

    res, res_string = check(0,0,"")
    # print("in check", p, s, cam, res)
    # print(cam)
    if res:
        return res, res_string
    return res,""


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        s = input()
        arr.append(s)
    
    init = arr[0]
    flag = True
    for i in range(1,n):
        res, res_string = solve(init,arr[i])
        # print(init, arr[i], res, res_string)
        if res:
            init = res_string
        else:
            flag=False
            break
    
    if flag is False:
        fin_res = '*'
    else:
        fin_res = ""
        for r in res_string:
            if r!="*":
                fin_res+=r

    res = "Case #{}: {}".format(_+1, fin_res)
    print(res)

