t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    res = 0
    arr = []
    i=0
    while i<l:
        if i<l-4 and s[i:i+5]=='twone':
            arr.append(i+3)
            i+=5
        elif i<l-2:
            if s[i:i+3]=='two':
                arr.append(i+2)
                i+=3
            elif s[i:i+3]=='one':
                arr.append(i+2)
                i+=3
            else:
                i+=1
        else:
            i+=1

    print(len(arr))
    print(*arr)