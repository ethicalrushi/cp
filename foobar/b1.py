dic = {}
def solve(top, h):
    if h==0:
        return

    diff = 2**h
    tl = top-diff
    tr = top-1
    dic[tl] = top
    dic[tr] = top
    solve(tl, h-1)
    solve(tr, h-1)

def solution(h, q):
    top = 2**h-1
    dic[top] = -1
    solve(top, h-1)
    res = [dic[e] for e in q]
    return res


n = int(input())
q = [int(x) for x in raw_input().strip().split()]
print(solution(n,q))


