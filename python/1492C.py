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

NQ=sys.stdin.readline().strip().split()
S=sys.stdin.readline().strip()
T=sys.stdin.readline().strip()
l=[]
r=[]
d={}
for i in range(len(S)):
    if S[i] not in d:
        d[S[i]]=[i]
    else:
        d[S[i]].append(i)
c=-1#current
i=0
while i<len(T):
    c+=1
    while S[c]!=T[i]:
        c+=1
    l.append(c)
    i+=1
c=len(S)#current
for i in range(len(T)-1,-1,-1):
    c-=1
    while S[c]!=T[i]:
        c-=1
    #c=d[T[i]][j]
    r.append(c)
r.reverse()
ans=0
for i in range(len(T)-1):
    ans=max(ans,r[i+1]-l[i])
#print(l,r)
print(ans)
#n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])
dd={"R":"L","L":"R"}
l=[0,0,1,1,3]
def tv(i,j,w):
    ma=-1
    mi=-1
    if i==j:
        return
    for k in range(i,j):
        if l[k]>ma:
            ma=l[k]
            mi=k
    ans[mi]=str(w)
    tv(i,mi,w+1)
    tv(mi+1,j,w+1)
l=[]
s=set()

#print(l[:20])
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

