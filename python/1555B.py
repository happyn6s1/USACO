"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
import math
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

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    m,n=list(map(int,sys.stdin.readline().strip().split()))
    x1,y1,x2,y2=list(map(int,sys.stdin.readline().strip().split()))
    x,y=list(map(int,sys.stdin.readline().strip().split()))
    w1=m-x2
    w2=x1
    
    h1=n-y2
    h2=y1
    M=max(m,n)+1
    ans=M
    if x+(x2-x1)>m and y+(y2-y1)>n:
        print(-1)
    else:
        if x+(x2-x1)<=m:
            if w1>=x or w2>=x:
                ans=0
            else:
                ans=min(ans,x-w1)
                ans=min(ans,x-w2)
        if y+(y2-y1)<=n:
            if h1>=y or h2>=y:
                ans=0
            else:
                ans=min(ans,y-h1)
                ans=min(ans,y-h2)
        print(ans*1.0)
        
    
