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
    ans=[]
    t=0
    m=0
    bt=0
    N=int(sys.stdin.readline().strip())
    st=sys.stdin.readline().strip()
    dq=deque([])
    tl=[]
    ml=[]
    F=True
    for i in range(N):
        c=st[i]
        if c=="M":
            if dq and dq[0]<i:
                dq.popleft()
                ml.append(i)
            else:
                F=False
                break
        else:
            dq.append(i)
    #print(dq,ml)
    if not F or len(dq)!=len(ml):
        print("NO")
    
    else:
        F=True
        for i in range(len(ml)):
            t=dq.popleft()
            if ml[i]>t:
                #print(i,ml,dq)
                F=False
                break
        if F:
            print("YES")
        else:
            print("NO")
            
