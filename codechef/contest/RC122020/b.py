t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    ls = s[1:]+s[0]
    rs = s[-1]+s[0:-1]
    if ls==rs:
        print("YES")
    else:
        print("NO")

