t = int(input())
for _ in range(t):
    n = int(input())
    dic = {'01':[],'10':[],'11':[],'00':[]}
    hash = {}
    bits = []
    for i in range(1,n+1):
        s = input()
        hash[s]=1
        bits.append(s)
        if s[0]=='0' and s[-1]=='1':
            dic['01'].append(i)
        elif s[0]=='1' and s[-1]=='0':
            dic['10'].append(i)
        elif s[0]=='1' and s[-1]=='1':
            dic['11'].append(i)
        else:
            dic['00'].append(i)
    
    a = len(dic['01'])
    b = len(dic['10'])
    c = len(dic['11'])
    d = len(dic['00'])

    res = 0

    #only one kind if bits at s and e
    if a==0 and b==0 and (c==0 or d==0): 
        print(0)
        print("")

    #impossible
    elif a==0 and b==0:
        print(-1)
    else:
        if a>b:
            res = (a-b)//2
            arr = []
            ind=0
            for e in dic['01']:
                if ind==res:
                    break
                rev= bits[e-1][::-1]
                if rev not in hash or hash[rev]==0:
                    arr.append(e)
                    hash[rev]=1
                    hash[bits[e-1]]=0
                    ind+=1
                
        else:
            res = (b-a)//2
            arr = []
            ind=0
            for e in dic['10']:
                if ind==res:
                    break
                rev = bits[e-1][::-1]
                if rev not in hash or hash[rev]==0:
                    hash[rev]=1
                    hash[bits[e-1]]=0
                    arr.append(e)
                    ind+=1
        
        if ind<res:
            print(-1)
        else:
            print(res)
            print(*arr)

            
        
                

        

    