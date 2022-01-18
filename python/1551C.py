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
    n,k=list(map(int,sys.stdin.readline().strip().split()))
    a=list(map(int,sys.stdin.readline().strip().split()))
    d={}
    for i in range(n):
        t=a[i]
        if t not in d:
            d[t]=[i]
        else:
            d[t].append(i)
    ans=[0 for _ in range(n)]
    tt=[]
    p=0
    for t in d:
        if len(d[t])>=k:
            for i in range(k):
                ans[d[t][i]]=i+1
        else:
            for i in range(len(d[t])):
                #ans[d[t][i]]=(p%k)
                #p+=1
                tt.append(d[t][i])
    for i in range(len(tt)-len(tt)%k):
        ans[tt[i]]=i%k+1
    for i in range(n):
        ans[i]=str(ans[i])
    print(" ".join(ans))
    
         
