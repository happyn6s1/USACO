"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
#from collections import defaultdict
import sys
import heapq
from collections import deque
MOD=1000000000007
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
#NK=sys.stdin.readline().strip().split()
K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0
def getlist(k,n,s):
    #print(k,n,s)
    if s<k*(k+1)//2 or s>(n+n+1-k)*k//2:
        return []
    if k==1:
        if s>=1 and s<=n:
            l=[s]
            return l
    for m in range(n,k-1,-1):
        ll=getlist(k-1,m-1,s-m)
        if len(ll)>0:
            l=[m]+ll
            return l
    return []        
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for testj in range(K):
    ans=0
    F=True
    #N=int(sys.stdin.readline().strip())+2
    n,l,r,s=list(map(int,sys.stdin.readline().strip().split()))
    k=r-l+1
    m0=k*(k+1)//2
    m1=(n+n+1-k)*k//2
    if s<m0 or s>m1:
        print(-1)
        continue
    ll=[]
    ll=getlist(k,n,s)
    #print(ll)
    if len(ll)==0: 
        print(-1)
    else:
        ss=set()
        for i in range(n):
            ss.add(i+1)
        ans=[0 for i in range(n+1)]
        for i in range(l,r+1):
             ans[i]=ll[i-l]
             #print(i,l,r,ll)
             ss.remove(ll[i-l])
        newss=list(ss)
        #print(newss)
        for i in range(1,n+1):
            if i >=l and i<=r:
                continue
            ans[i]=newss.pop()
        for i in range(n+1):
            ans[i]=str(ans[i])
        print(" ".join(ans[1:]))
             
             
        
    #print(" ".join(ll))
