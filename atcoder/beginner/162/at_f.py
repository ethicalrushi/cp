n = int(input())
a = [int(x) for x in input().strip().split()]



s1 = 0
s2=0
# print("d")
for i in range(0,n,2):
    # print(i)
    s1+=a[i]

for i in range(1,n,2):
    s2+=a[i]

# print(s1,s2,a[0],a[-1])

if n%2==1:
    s3 = s1-a[-1]
    s4 = s1-a[0]

    res = max(s3,s4,s2)
else:
    res = max(s1,s2)

print(res)



    