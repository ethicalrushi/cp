t = int(input())
for _ in range(t):
    n = int(input())
    bits = n//6+2
    offset = n%6
    a = int('1'+'0'*(bits-1),2)
    b = int('0'+'1'*(bits-1),2)
    c = int('1'*bits,2)
    
    