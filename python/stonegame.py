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
dd={"R":"L","L":"R"}
l=list(map(int,sys.stdin.readline().strip().split()))
d={}
for i in range(n):
    if l[i] not in d:
        d[l[i]]=1
    else:
        d[l[i]]+=1
dl=[]
for k in d:
    dl.append((k,d[k]))
dl.sort(reverse=True)
ans=0
t=0
b=(dl[0][1]+1)//2
lo=0
hi=-1
lo2=0
hi2=-1
c=0
tt=0
F=False
k=0
for k in range(len(dl)):
    if dl[k][1]%2==1:
        break
#print(dl,k)
if k<len(dl):
    lo=k
    lo2=k
    for i in range(dl[k][0],-1,-1):
        
        if i*3<=dl[k][0]:
            break
        a=0
        b=0
        for j in range(k,len(dl)):
            #print(i,j,k,dl)
            if dl[j][0]>=i:
                a+=dl[j][1]
            if dl[j][0]>=i*2:
                b+=dl[j][1]
            #print(i,j,a,b)
        print(i,a,b)
        if (a-b)%2==1:
            ans+=a-b
print(ans)
