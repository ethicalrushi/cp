for t in range(int(input())):
    n,l,r=map(int,input().split())
    b=1
    for i in range(1,n):
        a=b
        b+=2*(n-i)
        if l<b:
          break
    x,y=i,(l-a)//2+i+1
    b=(l-a)%2
    for _ in range(r-l):
        if b:
          print(y,end=" ")
          y+=1
          if y==n+1:
            x+=1
            y=x+1
        else:
          print(x,end=" ")
        b^=1
    if r==n*(n-1)+1:
        print(1)
    else:
        print(y if b else x)