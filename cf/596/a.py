
a, b= [int(x) for x in input().strip().split()]
if a==b:
    print(str(a)+'1',str(b)+'2')
elif b==a+1:
    print(str(a)+'9', str(b)+'0')
elif a==9 and b==1:
    print(str(a)+'9', str(b)+'00')
else:
    print(-1)