"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
#from collections import defaultdict
import sys
import math
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

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    ans=0
    n=int(sys.stdin.readline().strip())
    a=list(map(int,sys.stdin.readline().strip().split()))
    b=[]
    c=[]
    for t in a:
        if t%2==0:
            b.append(t)
        else:
            c.append(t)
    b.sort(reverse=True)
    c.sort(reverse=True)
    a=b+c
    for i in range(n-1):
        if a[i]%2==0:
            ans+=(n-1-i)
        else:
            for j in range(i+1,n):
                if math.gcd(a[i],a[j]*2)>1:
                    ans+=1
    print(ans)
