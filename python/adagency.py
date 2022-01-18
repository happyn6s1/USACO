"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque
MOD=1000000007
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
def factor(n,l,d):
    F=False
    for p in l:
        if n%p==0:
            if p in d:
                d[p]+=1
            else:
                d[p]=1
            F=True
            break
    if F:
        factor(n//p,l,d)
            
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
def find(parent,i):


    if parent[i] != i: 
        parent[i]=find(parent,parent[i]) 
    return parent[i] 

        # A utility function to do union of two subsets 
def union(parent,rank,xx,yy): 
    x=find(parent,xx)
    y=find(parent,yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
ans=0

#NQ=sys.stdin.readline().strip().split()

n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])

for j in range(n):
    AB=sys.stdin.readline().strip().split()
    #a=int(sys.stdin.readline().strip())
    a=int(AB[0])
    b=int(AB[1])
    #k=int(AB[2])
    #al=[0 for i in range(a)]
    #bl=[0 for i in range(b)]
    ak=sys.stdin.readline().strip().split()
    #bk=sys.stdin.readline().strip().split()
    ans=0
    h=[]
    d={}
    for i in range(a):
        ak[i]=int(ak[i])
        heapq.heappush(h,-ak[i])
        if -ak[i] not in d:
            d[-ak[i]]=1
        else:
            d[-ak[i]]+=1
    pre=-1
    c=0
    for i in range(b):
        k=heapq.heappop(h)
        if k!=pre:
            pre=k
            c=1
        else:
            c+=1
    ans=1    
    for i in range(c):
        ans*=(d[pre]-i)
    for i in range(c):
        ans=ans//(c-i)
    
    print(ans%MOD)


#    print("".join(l))
    #print(s)
    #l=sys.stdin.readline().strip().split()
    #s1=sys.stdin.readline().strip()
    #s2=sys.stdin.readline().strip()
    
        #print(pre,post,ll,rr,m1,m2,pre[ll],post[n-1-rr],post[n-1-rr][2])
    #if F:
    #    print("yes")
    #else:
    #    print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

