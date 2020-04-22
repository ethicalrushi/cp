t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    if n==1:
        res.append((1,1))
    else:
        # i = 0
        # while n>pow(2,i):
        #     n-=pow(2,i)
        #     i+=1

        num = "{0:b}".format(n)
        i = len(num)-1
        print(i)

        num1 = "1"*(i)

        n1 = int(num1,2)
        n-=n1 #remainder
        print(n)

        # turn =True
        # for j in range(1,i+1):
        #     temp = []
        #     for k in range(1,j+1):
        #         temp.append((j,k))
        #     if turn:
        #         res+=temp
        #         turn = False
        #     else:
        #         res+=temp[::-1]
        #         turn = True
        
        # j=res[-1][0]+1
        # m = res[-1][1]
        # for k in range(n):
        #     res.append((j,m))
        #     j+=1

    



    # print("Case #{}:".format(_+1))
    # for r in res:
    #     print(r[0], r[1])

    # print(len(res))
    