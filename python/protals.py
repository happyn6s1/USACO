"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
import sys

from collections import defaultdict

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
        
def find(i):
    if parent[i] != i: 
        parent[i]=find(parent[i]) 
    return parent[i] 


def union(xx,yy): 
    x=find(xx)
    y=find(yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
        
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
n=int(sys.stdin.readline().strip())
parent=[i for i in range(n*2)]
rank=[0 for i in range(n*2)]


ans=0
#print(ans)

#NQ=sys.stdin.readline().strip().split()

l=[]
for tn in range(n):
    l.append(list(map(int,sys.stdin.readline().strip().split())))
    union(l[-1][1]-1,l[-1][2]-1)
    union(l[-1][3]-1,l[-1][4]-1)

l.sort()
ss=set()
for i in range(n*2):
    ss.add(find(i))
k=len(ss)-1
F=False
#print(k)
for c in l:
    s=set()
    for i in range(1,5):
        s.add(find(c[i]-1))
    
    if len(s)>1:
        a,b=list(s)
        union(a,b)
        ans+=c[0]
        k-=1
        if k==0:
            F=True
            break
    if F:
        break
print(ans)
