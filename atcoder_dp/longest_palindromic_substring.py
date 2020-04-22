s = input()
n = len(s)

def reverse(s):
    r = ""
    r = s[::-1]
    return r

def solve(i):
    l = i-1
    h = i+1
    r = s[i]
    c=1
    while l>=0 and h<n and s[l]==s[h]:
        c+=2
        r +=s[h]
        l-=1
        h+=1
    
    res = reverse(r[1:])+r

    if i<n-1 and s[i]==s[i+1]:
        l1 = i-1
        h1 = i+2
        r1 = s[i]
        r2 = s[i+1]
        c1=2
        while l1>=0 and h1<n and s[l1]==s[h1]:
            c1+=2
            r1 = s[l1]+r1
            r2 = r2+s[h1]
            l1-=1
            h1+=1

        res1 = r1+r2
        print(i,c,c1,res,res1)
        if c1>c:
            c=c1
            res = res1

    return c,res

mn = 0
ans = ''
for i in range(n):
    c, res = solve(i)
    if mn<=c:
        mn = c
        ans = res

print(mn, ans)



