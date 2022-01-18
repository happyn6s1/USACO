"""
ID: happyn61
LANG: PYTHON3
PROB: castle
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
	
fin = open ('castle.in', 'r')
fout = open ('castle.out', 'w')
#print(dic["4734"])
NM=fin.readline().strip().split()
N=int(NM[0])
M=int(NM[1])
#pl=primes(M)

matrix = [[0]*N for i in range(M)]
matrixc = [[0]*N for i in range(M)]
matrixw = [[ [0]*2 for k in range(N) ]for i in range(M)] #E,N
#print(matrixw)
seta=set()
heapset=set()
for i in range(M):
    ll=fin.readline().strip().split()
    for j in range(N):
        matrix[i][j]=int(ll[j])
        seta.add(i*N+j)
#print(matrix)
#print(seta)
color=0
t=0
heapset.add(t)
colorct=[[]]
mc=0
while len(seta)>0:
    color+=1
    n=0
    t=seta.pop()
    heapset.add(t)
    seta.add(t)
    #print(t)
    while len(heapset)>0:
        #print(heapset)
        it=heapset.pop()
        #print(it)
        ii=it//N
        jj=it%N
        matrixc[ii][jj]=color
        n+=1
        seta.remove(it)
        #print(seta,heapset)
        k=15-matrix[ii][jj]
        #print(ii,jj)
        if k&1 and ii*N+jj-1 in seta:
            #print(ii*N+jj-1)
            heapset.add(ii*N+jj-1)
        if k&2 and (ii-1)*N+jj in seta:
            heapset.add((ii-1)*N+jj)
        if k&4 and ii*N+jj+1 in seta:
            heapset.add(ii*N+jj+1)
        if k&8 and (ii+1)*N+jj in seta:
            heapset.add((ii+1)*N+jj)
    #print(color,n)
    colorct.append(n)
    mc=max(n,mc)
            
    #print(ii,jj,matrix[ii][jj])

mw=0
a=0
b=0
c=""
for j in range(N-1,-1,-1):
    for i in range(M):    
        
        #print(matrix[i][j])
        k=matrix[i][j]
        if k&2 and i > 0 and matrixc[i][j]!=matrixc[i-1][j]:
            matrixw[i][j][0]=colorct[matrixc[i][j]]+colorct[matrixc[i-1][j]]
        #print(matrixc,i,j,k,colorct)
        if k&4 and j < N-1 and matrixc[i][j]!=matrixc[i][j+1]:
            #
            
            matrixw[i][j][1]=colorct[matrixc[i][j]]+colorct[matrixc[i][j+1]]

        if matrixw[i][j][1]>=mw:
            mw=matrixw[i][j][1]
            a=i
            b=j
            c="E"
        if matrixw[i][j][0]>=mw:
            mw=matrixw[i][j][0]
            a=i
            b=j
            c="N"
        
        #seta.add(i*N+j)
print(matrix)
print(matrixc)

print(matrixw)
print(color,mc,colorct)
print(a+1,b+1,c,mw)
fout.write (str(color)+"\n")
fout.write (str(mc)+"\n")
fout.write (str(mw)+"\n")
fout.write (str(a+1)+" "+str(b+1)+" "+c+"\n")
        

fout.close()
