"""
ID: happyn61
LANG: PYTHON3
PROB: pprime
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

#import heapq
def ispalindromel(l):
	ispalindrome=True
	for i in range(0,len(l)//2+1):
		if l[i] != l[-i-1]:
			ispalindrome=False
			break
	return ispalindrome
def n2l(n):
	l=[]
	while n>0:
		l.append(n%10)
		n=n//10
	#print (l)
	return l	
fin = open ('pprime.in', 'r')
fout = open ('pprime.out', 'w')
#print(dic["4734"])
NM=[int(i) for i in fin.readline().strip().split()]
N=NM[0]
#print(N)
M=NM[1]

mm=0
ll=[]
nl=[]
if N%2==0:
    N+=1

if M==100000000:
    M=9999999
    print(M)
pl=primesnm(N,M+1)

print(len(pl))

if M%2:
    M+=1
#print(pl)
#print(757 in pl)
n=0
for p in  pl:
    #print(p)
    fout.write (str(p)+"\n")
        
print(N,M)
print(n)
print(ll,nl)

fout.close()
