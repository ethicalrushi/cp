import sys
from collections import defaultdict

inputfiles = "bcdef"
for inp in inputfiles:
    infp = open(inp+'_a.txt', 'r')
    outp = open('ada/'+inp+'1_out.txt', 'w')
    sys.stdout = outp
    sys.stdin = infp

    b, l, d= [int(x) for x in input().split()]
    b_scores = [int(i) for i in input().split()]

    bk_count = defaultdict(lambda: 0)

    lib_data = []
    lib_bookid = []
    lib_bookscoreid = []

    for i in range(l):
        lib_data.append([int(x) for x in input().split()])
        lib_bookid.append([int(x) for x in input().split()])
        for bid in lib_bookid[-1]:
            bk_count[bid]+=1

    lib_signup = []
    for libd in lib_data:
        lib_signup.append(libd[1])

    lib_scores = []


    for lib_b in lib_bookid:
        temp = [b_scores[bid] for bid in lib_b]
        lib_scores.append(temp)

    for i in range(l):
        bids = lib_bookid[i]
        temp = [(b_scores[bid],bid) for bid in bids]
        temp.sort(reverse=True)
        lib_bookscoreid.append(temp)

    l_score_tot = []

    for i in range(l):
        time = lib_data[i][1]
        mxb = (d-time)*lib_data[1][2]
        cs = 0
        curr_score_arr = lib_bookscoreid[i]
        for j in range(min(len(curr_score_arr),mxb)):
            cs+= curr_score_arr[j][0]/bk_count[curr_score_arr[j][1]]**2
        l_score_tot.append(cs)

    factors = []
    for i in range(len(l_score_tot)):
        factors.append((l_score_tot[i]*lib_data[i][2]/lib_data[i][1],i))

    factors.sort(reverse=True)

    days = 0
    i=0
    sel_books = set([])
    fin_output = []
    while d>0 and i<l:
        sel_lib_id = factors[i][1]
        sel_signup = lib_data[sel_lib_id][1]  #signup time 
        d-=sel_signup
        b_count = 0
        mx = d*lib_data[sel_lib_id][2]  #MAX BOOKKS SENT
        curr_lib_book_op= []
        for sel_lib_bookscoreid in lib_bookscoreid[sel_lib_id]:
            cur_book_id = sel_lib_bookscoreid[1]
            if b_count>mx:
                break
            if cur_book_id not in sel_books:
                sel_books.add(cur_book_id)
                b_count+=1
                curr_lib_book_op.append(cur_book_id)
        i+=1
        if b_count>0:
            fin_output.append((sel_lib_id,curr_lib_book_op))
        



    print(len(fin_output))
    for res in fin_output:
        print(res[0], len(res[1]))
        print(*res[1])

