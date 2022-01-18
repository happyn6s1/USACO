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
#K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
n,m=list(map(int,sys.stdin.readline().strip().split()))
s=sys.stdin.readline().strip()
k=len(s)
a=[[0 for i in range(3)] for _ in range(3)]
l=[[0,0,0,0,0,0,0,0,0]]
d={"a":0,"b":1,"c":2}
for i in range(n):
    c=d[s[i]]
    k=l[-1].copy()
    k[c+3*(i%3)]+=1
    l.append(k)
#print(l)
for _ in range(m):
    r,q=list(map(int,sys.stdin.readline().strip().split()))
    a=[]
    for i in range(9):
        a.append(l[q][i]-l[r-1][i])
    #print(a)
    pp=[(0,4,8),(0,5,7),(1,3,8),(1,5,6),(2,4,6),(2,3,7)]
    ans=0
    for t1,t2,t3 in pp:
        ans=max(a[t1]+a[t2]+a[t3],ans)
        #print(r,q,ans)
    print(q-r+1-ans)
