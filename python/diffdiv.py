"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque

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
l=primes(30000)

for j in range(n):
    #AB=sys.stdin.readline().strip().split()
    s=int(sys.stdin.readline().strip())
    #b=list(sys.stdin.readline().strip())
    ans=0
    d={}
    #l=[]
    p=1
    a=b=0
    i=0
    aa=0
    t=1+s
    lo=0
    mi=0
    hi=len(l)-1
    while lo<=hi:
        mi=(lo+hi)//2
        
        if l[mi]>=t:
            a=l[mi]
            aa=mi
            hi=mi-1
        else:
            lo=mi+1
    #print(aa,a,"aa",t)
    lo=aa+1
    hi=len(l)-1
    t=a+s
    #print(lo,hi,t)
    while lo<=hi:
        mi=(lo+hi)//2
        if l[mi]>=t:
            b=l[mi]
            hi=mi-1
        else:
            lo=mi+1
     #   print(t,l[mi],b)
    print(a*b)
        #print(i,s,b)
        

    #print("".join(l))
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

