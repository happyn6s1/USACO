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
    N=int(sys.stdin.readline().strip())
    M=[]
    l=[]
    x1=x2=y1=y2=-1
    for i in range(N):
        st=list(sys.stdin.readline().strip())
        M.append(st)
        for j in range(N):
            if st[j]=="*":
                l.append((i,j))
            
    m=N
    n=N
    if l[0][0]==l[1][0]:
        k=(l[0][0]+1)%N
        M[k][l[1][1]]="*"
        M[k][l[0][1]]="*"
    elif l[0][1]==l[1][1]:
        k=(l[0][1]+1)%N
        M[l[0][0]][k]="*"
        M[l[1][0]][k]="*"
    else:
        M[l[0][0]][l[1][1]]="*"
        M[l[1][0]][l[0][1]]="*"
    for i in range(N):
        print("".join(M[i]))
    
    d={}
