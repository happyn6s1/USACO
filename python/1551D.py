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

#print(pp)
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    n=int(sys.stdin.readline().strip())
    l=[]
    for _ in range(n):
        l.append(sys.stdin.readline().strip())
    ans=0
    for k in ["a","b","c","d","e"]:
        tl=[]
        tt=[0,0]
        
        for w in l:
            ttt=0
            for c in w:
                if c==k:
                    ttt+=1
                else:
                    ttt-=1
            tl.append(ttt)
        tl.sort(reverse=True)
        tans=0
        tv=0
        #print(tl)
        if tl[0]>0:
            for v in tl:
                if tv+v>0:
                    tv+=v
                    tans+=1
                else:
                    break
            
        ans=max(ans,tans)
    print(ans)
