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

def ck(k,l):
    t=l[k]
    p=k
    ans=1
    for i in range(k-1,-1,-1):
        #print(l,p,i,t)
        if l[p]-l[i]>=t:
            ans+=1
            p=i
    #print("ret", l,k,ans)
    return ans
        
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    ans=0
    n=int(sys.stdin.readline().strip())
    l=[]
    e={}
    h=[]
    for i in range(n):
        l.append(list(map(int,sys.stdin.readline().strip().split())))
    for i in range(n-1):
        v,u=list(map(int,sys.stdin.readline().strip().split()))
        v-=1
        u-=1
        e[(v,u)]=False
    for v,u in e:
        for j,k in ((0,0),(0,1),(1,0),(1,1)):
            #heapq.heappush(h,(-abs(l[v][j]-l[u][k]),v,u,l[v][j],l[u][k]))
            h.append((-abs(l[v][j]-l[u][k]),v,u,l[v][j],l[u][k]))
        
    h.sort()
    #print(e)
    #print(h)
    m=0
    ii=0
    
    for ii in range((n-1)*4):
        #val,v,u,a,b=heapq.heappop(h)
        val,v,u,a,b=h[ii]
        if e[(v,u)] or a <l[v][0] or a>l[v][1] or b <l[u][0] or b>l[u][1]:
            continue
        l[v]=[a,a]
        l[u]=[b,b]
        m+=1
        ans+=(-val)
        e[(v,u)]=True
        ii+=1
        if m==n-1:
            break
        
    print(ans)
