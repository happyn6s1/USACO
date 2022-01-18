"""
ID: happyn61
LANG: PYTHON3
PROB: sprime
"""

#from collections import defaultdict
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def primesnm(m,n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    #print(sieve[757],m,n)
    ps=set()
    #for a in range(1,10):
    #    ps.add(a)
    for a in range(1,10):
        for b in range(0,10):
            ps.add(101*a+10*b)
            
    #print(ps)
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                ps.add(10001*a+1010*b+100*c)
                
    
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    ps.add(1000001*a+100010*b+10100*c+1000*d)
                    
                    
    #print(len(ps))    
    return  [i for i in range(m,n,2) if sieve[i] and (i in ps or i<12)]
def isprime2(n):
	if n == 2:
		#print("prime",n)
		return True
	for i in range(2,n):
		#print(i,n)
		if (n % i) ==0:
			return False
	
		#print("prime",n)
	return True
def isprime(n):
    if n == 2:
    #print("prime",n)
        return True
    if(n%2==0):
        return False
    #print(n)
    for i in range(3,int(n**0.5),2):
		#print(i,n)
        if (n % i) ==0:
            return False
	
		#print("prime",n)
    #print(n)
    return True    
def sprime(sl):
    rl=[]
    #print(sl)
    for i in sl:
        k=i*10
        for j in [1,3,7,9]:
            #print(k+j)
            if isprime(k+j):
                #print(k+j,"p")
                rl.append(k+j)
    #print(rl)
    return rl

#import heapq
	
fin = open ('sprime.in', 'r')
fout = open ('sprime.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())
M=10**(N)
#pl=primes(M)


n=[[2,3,5,7]]

for i in range(N-1):
    #print(i)
    n.append(sprime(n[i]))
print(n)

#nl=[[2, 3, 5, 7], [23, 29, 31, 37, 53, 59, 71, 73, 79], [233, 239, 293, 311, 313, 317, 373, 379, 593, 599, 719, 733, 739, 797], [2333, 2339, 2393, 2399, 2939, 3119, 3137, 3733, 3739, 3793, 3797, 5939, 7193, 7331, 7333, 7393], [23333, 23339, 23399, 23993, 29399, 31193, 31379, 37337, 37339, 37397, 59393, 59399, 71933, 73331, 73939], [233993, 239933, 293999, 373379, 373393, 593933, 593993, 719333, 739391, 739393, 739397, 739399], [2339933, 2399333, 2939999, 3733799, 5939333, 7393913, 7393931, 7393933], [23399339, 29399999, 37337999, 59393339, 73939133], []]

for p in  n[N-1]:
    #print(p)
    fout.write (str(p)+"\n")
        

fout.close()
