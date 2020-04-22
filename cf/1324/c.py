t = int(input())

for _ in range(t):
    a = input()
    a+='R'
    diff = []
    pi = -1

    for i in range(len(a)):
        if a[i]=='R':
            temp = i-pi
            pi = i
            diff.append(temp)
    
    # print(diff)
    print(max(diff))