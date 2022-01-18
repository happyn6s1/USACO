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

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for testj in range(K):
    ans=0
    #N=int(sys.stdin.readline().strip())
    a,b,c=list(map(int,sys.stdin.readline().strip().split()))
    a-=1
    b-=1
    c-=1
    if a==b:
        z=10**c
        if a==c:
            x=z
            y=z
        else:
            x=10**a
            x+=z
            y=x+z
        print(x,y)
    elif a>b:
        z=10**c
        if b==c:
            y=z
            x=10**a
            x+=z
        else:
            x=10**a
            y=10**b
            x+=(z*2)
            y+=z
        print(x,y)
    elif b>a:
        z=10**c
        if a==c:
            x=z
            y=10**b
            y+=z
        else:
            x=10**a
            y=10**b
            x+=z
            y+=(z*2)
        print(x,y)
        
