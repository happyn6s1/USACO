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
for _ in range(K):
    ans=[]
    e=[]
    o=[]
    F=True
    n=int(sys.stdin.readline().strip())
    
    u=list(map(int,sys.stdin.readline().strip().split()))
    s=list(map(int,sys.stdin.readline().strip().split()))
    #du=[]for i in range(n)]
    du={}
    for i in range(n):
        if u[i]-1 not in du:
            du[u[i]-1]=[s[i]]
        else:
            du[u[i]-1].append(s[i])
    for i in du:
        du[i].sort(reverse=True)
    for i in du:
        for j in range(1,len(du[i])):
            du[i][j]+=du[i][j-1]
    #print(du)
    for i in range(1,n+1):
        b=0
        for j in du: 
            l=du[j]
            a=len(l)
            #print(a,i,j,a//i*i-1)
            if a//i*i-1>=0:
                b+=(du[j][a//i*i-1])
        ans.append(str(b))
        
    print(" ".join(ans))
