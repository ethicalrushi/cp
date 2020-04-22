n = int(input())
a = input()
b = ''
for a_ in a:
    s = ord(a_)+n
    while s>ord('Z'):
        s = s-ord('Z')+ord('A')-1

    b+= chr(s)
print(b)