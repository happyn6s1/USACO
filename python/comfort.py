"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
import math
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
d={}
ed={}
qe=deque([])
ss=set()
for i in range(n):
    XY=sys.stdin.readline().strip().split()
    x=int(XY[0])
    y=int(XY[1])
    if (x,y) in ed:
        d[(x,y)]=ed[(x,y)]
        del ed[(x,y)]
        print(len(ed))
        continue
    c=[(0,1),(1,0),(0,-1),(-1,0)]
    v=0
    qe.append((x,y,0))
    ss.add((x,y))
    while qe:
        v=0
        x,y,w=qe.popleft()

        #ss.add((x,y))
        #print(x,y,w,d)
        if w==0:
            d[(x,y)]=0
        else:
            ed[(x,y)]=0
        for a,b in c:
            #update neighbor
            if (x+a,y+b) in d:
                v+=1
                d[(x+a,y+b)]+=1
                if d[(x+a,y+b)]==3:
                    for p,q in c:
                        if (x+a+p,y+b+q) not in ss:
                            ss.add((x+a+p,y+b+q))
                            qe.append((x+a+p,y+b+q,1))
                            break
            if (x+a,y+b) in ed:
                v+=1
                ed[(x+a,y+b)]+=1
                if ed[(x+a,y+b)]==3:
                    for p,q in c:
                        if (x+a+p,y+b+q) not in ss:
                            qe.append((x+a+p,y+b+q,1))
                            ss.add((x+a+p,y+b+q))
                            break
        if w==0:
            d[(x,y)]=v
            if v==3:
                for p,q in c:
                        if (x+p,y+q) not in ss:
                            ss.add((x+p,y+q))
                            qe.append((x+p,y+q,1))
                            break
        else:
            ed[(x,y)]=v
            if v==3:
                for p,q in c:
                        if (x+p,y+q) not in ss:
                            ss.add((x+p,y+q))
                            qe.append((x+p,y+q,1))
                            break
        
    #print(d,ed)
    print(len(ed))
