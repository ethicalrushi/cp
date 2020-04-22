t = int(input())
for _ in range(t):
    s = input()
    init = 0

    ans = ""
    for e in s:
        if init<int(e):
            ans+='('*(int(e)-init)
        else:
            ans+=')'*(init-int(e))
        ans+=e
        init = int(e)
    
    ans+=')'*int(s[-1])

    res = "Case #{}: {}".format(_+1, ans)
    print(res)

