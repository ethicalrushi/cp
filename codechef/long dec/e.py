mod = 10**9+7

N = 100001

factorialNumInverse = [None] * (N + 1) 

naturalNumInverse = [None] * (N + 1) 

fact = [None] * (N + 1) 

p = mod
InverseofNumber(p) 
InverseofFactorial(p) 
factorial(p) 

def InverseofNumber(p): 
	naturalNumInverse[0] = naturalNumInverse[1] = 1
	for i in range(2, N + 1, 1): 
		naturalNumInverse[i] = (naturalNumInverse[p % i] *
								(p - int(p / i)) % p) 

def InverseofFactorial(p): 
	factorialNumInverse[0] = factorialNumInverse[1] = 1

	for i in range(2, N + 1, 1): 
		factorialNumInverse[i] = (naturalNumInverse[i] *
								factorialNumInverse[i - 1]) % p 

def factorial(p): 
	fact[0] = 1

	for i in range(1, N + 1): 
		fact[i] = (fact[i - 1] * i) % p 

def Binomial(N, R, p): 
	
	# n C r = n!*inverse(r!)*inverse((n-r)!) 
	ans = ((fact[N] * factorialNumInverse[R])% p *
					factorialNumInverse[N - R])% p 
	return ans 


t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    a=0
    b=0
    for i in range(n):
        if s1[i]=='1':
            a+=1
        if s2[i]=='1':
            b+=1
    
    mn = abs(a-b)
    if a+b>n:
        mx = a+b-2*(a+b-n)
    else:
        mx = a+b

    res=0

    for i in range(mn,mx+1,2):
        res= (res%mod+Binomial(n,i,mod)%mod)%mod
    print(res)





# fac = [None for i in range(10**5+2)]
# fac[0]=1

# for i in range(1,10**5+2):
#     fac[i] = ((i%mod)*(fac[i-1]%mod))%mod

# def modinverse(n,mod):
#     return pow(n,mod-2,mod)

# def ncr(n,i):
#     num = fac[n]
#     return (num*((modinverse(fac[i],mod)*modinverse(fac[n-i],mod))%mod))%mod

# def calt(t,n,i,p):
#     num = (t*(n-i-2)*(n-i-1))%p
#     return (num*((modinverse(i+1,mod)*modinverse(i+2,mod))%mod))%mod
