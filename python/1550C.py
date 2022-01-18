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
    n=int(sys.stdin.readline().strip())
    #n,a,b=list(map(int,sys.stdin.readline().strip().split()))
    l=list(map(int,sys.stdin.readline().strip().split()))
    uh=[]
    dh=[]
    lo=0
    hi=2
    if len(l)<3:
        print(n*2-1)
    else:
        ans=n*2-1
        heapq.heappush(uh,(l[0],0))
        heapq.heappush(uh,(l[1],1))
        #heapq.heappush(uh,(l[2],2))
        
        heapq.heappush(dh,(-l[0],0))
        heapq.heappush(dh,(-l[1],1))
        #heapq.heappush(dh,(-l[2],2))
        #print(ans)
        for hi in range(2,n):
            #print(uh,dh)
            heapq.heappush(uh,(l[hi],hi))
        
            heapq.heappush(dh,(-l[hi],hi))
            while hi-lo>=2 and uh[0][1] == hi and dh[0][1]==lo or uh[0][1] == lo and dh[0][1]==hi:
                heapq.heappop(uh)
                heapq.heappop(dh)
                lo+=1
                
            print(hi,lo,hi-lo,dh,uh)
            if hi-lo>=2:
                t=hi-lo-1
                ans+=t
        print(ans)
